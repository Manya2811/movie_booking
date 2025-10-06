from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from .models import Movie, Show
from .serializers import MovieSerializer, ShowSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from .models import Booking 
from .serializers import BookingSerializer 

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ShowListView(generics.ListAPIView):
    serializer_class = ShowSerializer

    def get_queryset(self):
        movie_id = self.kwargs['id']
        return Show.objects.filter(movie_id=movie_id)    
    

class BookSeatView(APIView):
    permission_classes = [IsAuthenticated] # Ensures only logged-in users can access this

    def post(self, request, id): # 'id' here is the Show ID
        try:
            show = Show.objects.get(pk=id)
        except Show.DoesNotExist:
            return Response({'error': 'Show not found.'}, status=status.HTTP_404_NOT_FOUND)

        seat_number = request.data.get('seat_number')

        if not seat_number:
            return Response({'error': 'Seat number is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # This transaction block prevents race conditions
        with transaction.atomic():
            # Rule: Prevent overbooking
            booked_seats_count = Booking.objects.filter(show=show, status='booked').count()
            if booked_seats_count >= show.total_seats:
                return Response({'error': 'This show is sold out.'}, status=status.HTTP_400_BAD_REQUEST)

            # Rule: Prevent double booking
            is_seat_booked = Booking.objects.filter(show=show, seat_number=seat_number, status='booked').exists()
            if is_seat_booked:
                return Response({'error': 'This seat is already booked.'}, status=status.HTTP_400_BAD_REQUEST)

            # If all rules pass, create the booking
            booking = Booking.objects.create(user=request.user, show=show, seat_number=seat_number)
            serializer = BookingSerializer(booking)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class CancelBookingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id): # 'id' here is the Booking ID
        try:
            booking = Booking.objects.get(pk=id)

            # Security Rule: A user can only cancel their OWN booking
            if booking.user != request.user:
                return Response({'error': 'You do not have permission to cancel this booking.'}, status=status.HTTP_403_FORBIDDEN)

            if booking.status == 'cancelled':
                return Response({'error': 'This booking has already been cancelled.'}, status=status.HTTP_400_BAD_REQUEST)

            # Rule: Cancelling frees up the seat
            booking.status = 'cancelled'
            booking.save()

            serializer = BookingSerializer(booking)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Booking.DoesNotExist:
            return Response({'error': 'Booking not found.'}, status=status.HTTP_404_NOT_FOUND)    
        
class MyBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)        
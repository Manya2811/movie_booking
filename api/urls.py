from django.urls import path
from .views import SignupView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignupView, MovieListView, ShowListView, BookSeatView, CancelBookingView, MyBookingsView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:id>/shows/', ShowListView.as_view(), name='show-list'),
    path('shows/<int:id>/book/', BookSeatView.as_view(), name='book-seat'),
    path('bookings/<int:id>/cancel/', CancelBookingView.as_view(), name='cancel-booking'),
    path('my-bookings/', MyBookingsView.as_view(), name='my-bookings'),
]
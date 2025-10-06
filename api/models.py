from django.db import models
from django.contrib.auth.models import User

# Represents a movie with a title and duration
class Movie(models.Model):
    title = models.CharField(max_length=255)
    duration_minutes = models.IntegerField()

    def __str__(self):
        return self.title

# Represents a specific screening of a movie
class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # Link to Movie
    screen_name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    total_seats = models.IntegerField()

    def __str__(self):
        return f"{self.movie.title} at {self.screen_name} on {self.date_time}"

# Represents a user's booking for a show
class Booking(models.Model):
    STATUS_CHOICES = (
        ('booked', 'Booked'),
        ('cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Link to the User
    show = models.ForeignKey(Show, on_delete=models.CASCADE) # Link to the Show
    seat_number = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='booked')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.user.username} - Seat {self.seat_number}"
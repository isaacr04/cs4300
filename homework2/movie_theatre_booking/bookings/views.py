from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from datetime import date

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    seats = Seat.objects.filter(booking_status=False)
    if request.method == 'POST':
        user_name = request.POST.get('user')
        seat_id = request.POST.get('seat')
        seat = Seat.objects.get(pk=seat_id)
        seat.booking_status = True
        seat.save()
        Booking.objects.create(
            movie=movie,
            seat=seat,
            user=user_name,
            booking_date=date.today()
        )
        return redirect('booking_history')
    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

def booking_history(request):
    bookings = Booking.objects.all().order_by('-booking_date')
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})

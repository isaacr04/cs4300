from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from datetime import date, timedelta

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
    seats = Seat.objects.filter(is_booked=False)
    if request.method == 'POST':
        user_name = request.POST.get('user')
        seat_id = request.POST.get('seat')
        seat = Seat.objects.get(pk=seat_id)
        seat.is_booked = True
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


def seed_database(request):
    """Seed the database with sample movies and 30 seats each."""

    movies_data = [
        {
            "title": "Interstellar",
            "description": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.",
            "release_date": "2014-11-07",
            "duration_minutes": 169,
        },
        {
            "title": "Inception",
            "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project and his team to disaster.",
            "release_date": "2010-07-16",
            "duration_minutes": 148,
        },
        {
            "title": "The Dark Knight",
            "description": "When a menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman, James Gordon and Harvey Dent must work together to put an end to the madness.",
            "release_date": "2008-07-18",
            "duration_minutes": 152,
        },
        {
            "title": "Dune: Part One",
            "description": "Paul Atreides arrives on Arrakis after his father accepts the stewardship of the dangerous planet. However, chaos ensues after a betrayal as forces clash to control melange, a precious resource.",
            "release_date": "2021-10-22",
            "duration_minutes": 155,
        },
        {
            "title": "Avatar",
            "description": "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
            "release_date": "2009-12-18",
            "duration_minutes": 162,
        },
    ]

    created_movies = 0
    created_seats = 0

    for data in movies_data:
        # Convert duration_minutes to timedelta
        duration = timedelta(minutes=data.pop('duration_minutes'))

        movie, made = Movie.objects.get_or_create(
            title=data["title"],
            defaults={
                "description": data["description"],
                "release_date": data["release_date"],
                "duration": duration,
            }
        )

        if made:
            created_movies += 1

        # Create 30 seats for this movie if they don't already exist
        existing_seats = Seat.objects.filter(movie=movie).count()
        seats_to_create = 30 - existing_seats

        if seats_to_create > 0:
            seats = [
                Seat(movie=movie, seat_number=i + 1)
                for i in range(existing_seats, existing_seats + seats_to_create)
            ]
            Seat.objects.bulk_create(seats)
            created_seats += len(seats)

    return Response({
        "message": "Seed complete",
        "movies_created": created_movies,
        "seats_created": created_seats
    }, status=status.HTTP_201_CREATED)
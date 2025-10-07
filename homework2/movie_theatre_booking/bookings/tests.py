from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date, timedelta
from bookings.models import Movie, Seat, Booking

# -----------------------------
# Test models
# -----------------------------

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test description.",
            release_date=date(2024, 1, 1),
            duration=timedelta(minutes=120)
        )

    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Test Movie")

    def test_movie_fields(self):
        self.assertEqual(self.movie.description, "A test description.")
        self.assertEqual(self.movie.release_date, date(2024, 1, 1))
        self.assertEqual(self.movie.duration, timedelta(minutes=120))


class SeatModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Seat Movie",
            description="Movie for seat testing.",
            release_date=date(2024, 2, 1),
            duration=timedelta(minutes=100)
        )
        self.seat = Seat.objects.create(seat_number=5, movie=self.movie)

    def test_seat_str(self):
        self.assertEqual(str(self.seat), f"Seat 5 for {self.movie.title}")

    def test_seat_is_booked_default(self):
        seat = Seat.objects.create(seat_number=6, movie=self.movie)
        self.assertFalse(seat.is_booked)


class BookingModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Another Movie",
            description="Description",
            release_date=date(2024, 2, 2),
            duration=timedelta(minutes=90)
        )
        self.seat = Seat.objects.create(seat_number=10, movie=self.movie)
        self.booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user="Alice",
            booking_date=date(2024, 3, 3)
        )

    def test_booking_str(self):
        expected_str = f"Alice booked {self.seat} for {self.movie}"
        self.assertEqual(str(self.booking), expected_str)

    def test_booking_relationships(self):
        self.assertEqual(self.booking.movie.title, "Another Movie")
        self.assertEqual(self.booking.seat.seat_number, 10)
        self.assertEqual(self.booking.user, "Alice")

    def test_booking_date(self):
        self.assertEqual(self.booking.booking_date, date(2024, 3, 3))


# -----------------------------
# Test API endpoints
# -----------------------------

class MovieAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie_data = {
            "title": "API Movie",
            "description": "Made via API",
            "release_date": "2024-05-05",
            "duration": "02:00:00"
        }

    def test_create_movie(self):
        response = self.client.post('/api/movies/', self.movie_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)

    def test_list_movies(self):
        Movie.objects.create(
            title="List Movie",
            description="For listing",
            release_date=date(2024, 5, 6),
            duration=timedelta(minutes=120)
        )
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)


class SeatAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(
            title="Seat API Movie",
            description="Movie for API seat test",
            release_date=date(2024, 5, 7),
            duration=timedelta(minutes=90)
        )
        # Automatically create a seat for this movie
        self.seat = Seat.objects.create(seat_number=1, movie=self.movie)
        self.seat_data = {"seat_number": 2, "movie": self.movie.id}

    def test_create_seat(self):
        response = self.client.post('/api/seats/', self.seat_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Seat.objects.count(), 2)

    def test_list_seats(self):
        response = self.client.get('/api/seats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)


class BookingAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(
            title="Bookable",
            description="For booking test",
            release_date=date(2024, 6, 1),
            duration=timedelta(minutes=100)
        )
        # Automatically create a seat for booking
        self.seat = Seat.objects.create(seat_number=1, movie=self.movie)
        self.booking_data = {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "user": "Bob",
            "booking_date": "2024-06-10"
        }

    def test_create_booking(self):
        response = self.client.post('/api/bookings/', self.booking_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)

    def test_list_bookings(self):
        Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user="Charlie",
            booking_date=date(2024, 6, 12)
        )
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

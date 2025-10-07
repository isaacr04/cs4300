from django.core.management.base import BaseCommand
from bookings.models import Movie, Seat
from datetime import date, timedelta

class Command(BaseCommand):
    help = "Seed the database with sample movies and 30 seats each."

    def handle(self, *args, **options):
        movies = [
            {
                "title": "Interstellar",
                "description": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.",
                "release_date": date(2014, 11, 7),
                "duration": timedelta(minutes=169),
            },
            {
                "title": "Inception",
                "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project and his team to disaster.",
                "release_date": date(2010, 7, 16),
                "duration": timedelta(minutes=148),
            },
            {
                "title": "The Dark Knight",
                "description": "When a menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman, James Gordon and Harvey Dent must work together to put an end to the madness.",
                "release_date": date(2008, 7, 18),
                "duration": timedelta(minutes=152),
            },
            {
                "title": "Dune: Part One",
                "description": "Paul Atreides arrives on Arrakis after his father accepts the stewardship of the dangerous planet. However, chaos ensues after a betrayal as forces clash to control melange, a precious resource.",
                "release_date": date(2021, 10, 22),
                "duration": timedelta(minutes=155),
            },
            {
                "title": "Avatar",
                "description": "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                "release_date": date(2009, 12, 18),
                "duration": timedelta(minutes=162),
            },
        ]

        created_movies = 0
        created_seats = 0

        for data in movies:
            movie, made = Movie.objects.get_or_create(title=data["title"], defaults=data)
            if made:
                created_movies += 1

            # Create 30 seats for this movie if they don't already exist
            existing_seats = Seat.objects.filter(movie=movie).count()
            seats_to_create = 30 - existing_seats
            seats = [Seat(movie=movie, seat_number=i+1) for i in range(existing_seats, existing_seats + seats_to_create)]
            Seat.objects.bulk_create(seats)
            created_seats += len(seats)

        self.stdout.write(self.style.SUCCESS(
            f"Seed complete: {created_movies} new movies added, {created_seats} seats created."
        ))

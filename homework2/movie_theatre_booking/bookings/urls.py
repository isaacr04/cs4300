from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, book_seat, booking_history, seed_database

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('book/<int:movie_id>/', book_seat, name='book_seat'),
    path('history/', booking_history, name='booking_history'),
    path('api/', include(router.urls)),
    path('api/seed/', seed_database, name='seed_database'),
]

from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('my-reviews/', views.my_reviews_view, name='my-reviews'),
    path('review/<int:tmdb_id>/<str:movie_title>/', views.review_form_view, name='review-form'),
]

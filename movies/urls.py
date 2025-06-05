from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('search/', views.search_view, name='search'),
    path('genre/', views.genre_view, name='genre-list'),  # <-- add this line
    path('detail/<int:tmdb_id>/', views.detail_view, name='detail'),
    path('list/', views.list_view, name='watchlist'),
]

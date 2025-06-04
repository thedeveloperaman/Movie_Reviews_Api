from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('search/', views.search_view, name='search'),
    path('detail/<int:tmdb_id>/', views.detail_view, name='detail'),
    path('list/', views.list_view, name='watchlist'),
    # path('watchlist/add/<int:tmdb_id>/', views.add_to_watchlist, name='add_to_watchlist'),
]

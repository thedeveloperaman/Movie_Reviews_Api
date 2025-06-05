from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('trending/', views.trending_movies, name='trending'),
    path('coming-soon/', views.coming_soon, name='coming-soon'),
    path('favorites/', views.favorites, name='favorites'),
    path('watch-later/', views.watch_later, name='watch-later'),
]

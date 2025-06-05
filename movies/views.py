from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .tmdb import search_movies, get_movie_details, get_movies_by_genre
from .models import SavedMovie
from reviews.models import Review  # Add this import
from django.conf import settings
import requests

def search_view(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        data = search_movies(query)
        results = data.get('results', [])
    return render(request, 'search.html', {'results': results, 'query': query})

def detail_view(request, tmdb_id):
    movie = get_movie_details(tmdb_id)
    movie_reviews = Review.objects.filter(tmdb_id=tmdb_id).order_by('-created_at')  # Only this movie's reviews
    return render(request, 'detail.html', {'movie': movie, 'reviews': movie_reviews})

@login_required
def list_view(request):
    saved_movies = SavedMovie.objects.filter(user=request.user).order_by('-added_at')
    return render(request, 'list.html', {'saved_movies': saved_movies})

def genre_view(request):
    genre = request.GET.get('genre', '')
    movies = []
    genre_title = ''
    if genre == 'top':
        # Show all top-rated movies
        api_key = settings.TMDB_API_KEY
        base_url = settings.TMDB_API_BASE_URL
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json;charset=utf-8"
        }
        url = f"{base_url}/movie/top_rated"
        params = {"language": "en-US", "page": 1}
        resp = requests.get(url, headers=headers, params=params)
        if resp.status_code == 200:
            movies = resp.json().get('results', [])
        genre_title = "Top"
    elif genre == 'adventure':
        from .tmdb import get_movies_by_genre
        movies = get_movies_by_genre('adventure', limit=40)
        genre_title = "Adventure"
    else:
        # fallback or handle other genres as needed
        pass
    return render(request, 'genre_list.html', {
        'movies': movies,
        'genre_title': genre_title,
    })

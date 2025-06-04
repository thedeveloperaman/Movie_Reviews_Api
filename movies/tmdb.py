import requests
from django.conf import settings

TMDB_API_KEY = getattr(settings, 'TMDB_API_KEY', None)
TMDB_API_BASE_URL = getattr(settings, 'TMDB_API_BASE_URL', 'https://api.themoviedb.org/3')

def get_tmdb_headers():
    return {
        "Authorization": f"Bearer {TMDB_API_KEY}",
        "Content-Type": "application/json;charset=utf-8"
    }

def search_movies(query, page=1):
    url = f"{TMDB_API_BASE_URL}/search/movie"
    params = {
        "query": query,
        "page": page,
        "include_adult": False,
        "language": "en-US"
    }
    response = requests.get(url, headers=get_tmdb_headers(), params=params)
    response.raise_for_status()
    return response.json()

def get_movie_details(movie_id):
    url = f"{TMDB_API_BASE_URL}/movie/{movie_id}"
    params = {"language": "en-US"}
    response = requests.get(url, headers=get_tmdb_headers(), params=params)
    response.raise_for_status()
    return response.json()

def get_trending_movies(time_window="week"):
    url = f"{TMDB_API_BASE_URL}/trending/movie/{time_window}"
    params = {"language": "en-US"}
    response = requests.get(url, headers=get_tmdb_headers(), params=params)
    response.raise_for_status()
    return response.json()

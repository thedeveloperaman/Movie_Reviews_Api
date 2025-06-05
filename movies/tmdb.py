import requests
from django.conf import settings

TMDB_API_KEY = getattr(settings, 'TMDB_API_KEY', None)
TMDB_API_BASE_URL = getattr(settings, 'TMDB_API_BASE_URL', 'https://api.themoviedb.org/3')

GENRE_MAP = {
    "action": 28,
    "adventure": 12,
    "comedy": 35,
    "animation": 16,
    "crime": 80,
    "documentary": 99,
    "drama": 18,
    "family": 10751,
    "fantasy": 14,
    "history": 36,
    "horror": 27,
    "music": 10402,
    "mystery": 9648,
    "romance": 10749,
    "science fiction": 878,
    "tv movie": 10770,
    "thriller": 53,
    "war": 10752,
    "western": 37,
}

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

def get_movies_by_genre(genre_name, page=1, limit=8):
    genre_id = GENRE_MAP.get(genre_name.lower())
    if not genre_id:
        return []

    url = f"{TMDB_API_BASE_URL}/discover/movie"
    params = {
        "with_genres": genre_id,
        "sort_by": "popularity.desc",
        "page": page,
        "language": "en-US"
    }
    response = requests.get(url, headers=get_tmdb_headers(), params=params)
    response.raise_for_status()
    results = response.json().get("results", [])[:limit]
    # Optionally, map genre IDs to names
    for movie in results:
        movie["genres"] = [genre_name.capitalize()]
    return results

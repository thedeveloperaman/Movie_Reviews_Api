import requests
from django.conf import settings
from django.shortcuts import render, redirect
from movies.models import SavedMovie
from movies.tmdb import get_movies_by_genre

def home(request):
    api_key = settings.TMDB_API_KEY
    base_url = settings.TMDB_API_BASE_URL
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json;charset=utf-8"
    }

    # New Movies (Now Playing)
    new_movies = []
    url_now_playing = f"{base_url}/movie/now_playing"
    params = {"language": "en-US", "page": 1}
    resp_new = requests.get(url_now_playing, headers=headers, params=params)
    if resp_new.status_code == 200:
        new_movies = resp_new.json().get('results', [])[:12]

    # Top Movies (Top Rated)
    top_movies = []
    url_top_rated = f"{base_url}/movie/top_rated"
    resp_top = requests.get(url_top_rated, headers=headers, params=params)
    if resp_top.status_code == 200:
        top_movies = resp_top.json().get('results', [])[:12]

    adventure_movies = get_movies_by_genre('adventure', limit=8)
    action_movies = get_movies_by_genre('action', limit=8)
    funny_movies = get_movies_by_genre('comedy', limit=8)
    return render(request, "home.html", {
        "new_movies": new_movies,
        "top_movies": top_movies,
        "adventure_movies": adventure_movies,
        "action_movies": action_movies,
        "funny_movies": funny_movies,
    })

def trending_movies(request):
    api_key = settings.TMDB_API_KEY
    base_url = settings.TMDB_API_BASE_URL
    url = f"{base_url}/trending/movie/week"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json;charset=utf-8"
    }
    params = {"language": "en-US"}
    response = requests.get(url, headers=headers, params=params)
    movies = []
    if response.status_code == 200:
        movies = response.json().get('results', [])
    return render(request, "movies_list.html", {
        "section_title": "Trending Movies",
        "movies": movies,
    })

def coming_soon(request):
    api_key = settings.TMDB_API_KEY
    base_url = settings.TMDB_API_BASE_URL
    url = f"{base_url}/movie/upcoming"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json;charset=utf-8"
    }
    params = {"language": "en-US"}
    response = requests.get(url, headers=headers, params=params)
    movies = []
    if response.status_code == 200:
        movies = response.json().get('results', [])
    return render(request, "movies_list.html", {
        "section_title": "Coming Soon",
        "movies": movies,
    })

def favorites(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    # You can add a "favorite" boolean field to SavedMovie if you want to distinguish favorites
    movies = SavedMovie.objects.filter(user=request.user)
    return render(request, "movies_list.html", {
        "section_title": "My Favorites",
        "movies": movies,
        "is_saved": True,
    })

def watch_later(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    movies = SavedMovie.objects.filter(user=request.user)
    return render(request, "movies_list.html", {
        "section_title": "Watch Later",
        "movies": movies,
        "is_saved": True,
    })

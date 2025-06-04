from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .tmdb import search_movies, get_movie_details
from .models import SavedMovie

def search_view(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        data = search_movies(query)
        results = data.get('results', [])
    return render(request, 'search.html', {'results': results, 'query': query})

def detail_view(request, tmdb_id):
    movie = get_movie_details(tmdb_id)
    return render(request, 'detail.html', {'movie': movie})

@login_required
def list_view(request):
    saved_movies = SavedMovie.objects.filter(user=request.user).order_by('-added_at')
    return render(request, 'list.html', {'saved_movies': saved_movies})

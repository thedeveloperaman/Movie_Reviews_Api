from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MovieList, MovieListItem
from .forms import MovieListForm

@login_required
def my_lists_view(request):
    lists = MovieList.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_lists.html', {'lists': lists})

@login_required
def list_detail_view(request, list_id):
    movie_list = get_object_or_404(MovieList, id=list_id, user=request.user)
    items = movie_list.items.all().order_by('-added_at')
    return render(request, 'list_detail.html', {'movie_list': movie_list, 'items': items})

@login_required
def create_list_view(request):
    if request.method == 'POST':
        form = MovieListForm(request.POST)
        if form.is_valid():
            movie_list = form.save(commit=False)
            movie_list.user = request.user
            movie_list.save()
            return redirect('lists:my-lists')
    else:
        form = MovieListForm()
    return render(request, 'list_form.html', {'form': form})

@login_required
def delete_movie_from_list(request, list_id, item_id):
    movie_list = get_object_or_404(MovieList, id=list_id, user=request.user)
    item = get_object_or_404(MovieListItem, id=item_id, movie_list=movie_list)
    if request.method == 'POST':
        item.delete()
        return redirect('lists:list-detail', list_id=list_id)
    return redirect('lists:list-detail', list_id=list_id)

@login_required
def add_movie_to_list(request, list_id):
    movie_list = get_object_or_404(MovieList, id=list_id, user=request.user)
    if request.method == 'POST':
        tmdb_id = request.POST.get('tmdb_id')
        title = request.POST.get('title')
        poster_path = request.POST.get('poster_path')
        # Prevent duplicates
        if not movie_list.items.filter(tmdb_id=tmdb_id).exists():
            MovieListItem.objects.create(
                movie_list=movie_list,
                tmdb_id=tmdb_id,
                title=title,
                poster_path=poster_path
            )
    return redirect('lists:list-detail', list_id=list_id)

@login_required
def edit_list_view(request, list_id):
    movie_list = get_object_or_404(MovieList, id=list_id, user=request.user)
    if request.method == 'POST':
        form = MovieListForm(request.POST, instance=movie_list)
        if form.is_valid():
            form.save()
            return redirect('lists:my-lists')
    else:
        form = MovieListForm(instance=movie_list)
    return render(request, 'list_form.html', {'form': form, 'edit_mode': True})

@login_required
def delete_list_view(request, list_id):
    movie_list = get_object_or_404(MovieList, id=list_id, user=request.user)
    if request.method == 'POST':
        movie_list.delete()
        return redirect('lists:my-lists')
    return redirect('lists:my-lists')

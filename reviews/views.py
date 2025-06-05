from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from movies.tmdb import get_movie_details

def all_reviews_view(request):
    reviews = Review.objects.all().order_by('-created_at')
    for review in reviews:
        try:
            movie = get_movie_details(review.tmdb_id)
            review.movie_poster = movie.get('poster_path')
        except Exception:
            review.movie_poster = ''
    return render(request, 'all_reviews.html', {'reviews': reviews})

@login_required
def my_reviews_view(request):
    reviews = Review.objects.filter(user=request.user).order_by('-created_at')
    # Attach poster path to each review
    for review in reviews:
        try:
            movie = get_movie_details(review.tmdb_id)
            review.movie_poster = movie.get('poster_path')
        except Exception:
            review.movie_poster = ''
    return render(request, 'my_reviews.html', {'reviews': reviews})

@login_required
def review_form_view(request, tmdb_id, movie_title):
    review = Review.objects.filter(user=request.user, tmdb_id=tmdb_id).first()
    if request.method == 'POST':
        if review:
            form = ReviewForm(request.POST, instance=review)
        else:
            form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.tmdb_id = tmdb_id
            review.movie_title = movie_title
            review.save()
            return redirect('reviews:my-reviews')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review_form.html', {'form': form, 'movie_title': movie_title})

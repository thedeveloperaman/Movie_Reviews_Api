from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm

@login_required
def my_reviews_view(request):
    reviews = Review.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_reviews.html', {'reviews': reviews})

@login_required
def review_form_view(request, tmdb_id, movie_title):
    # movie_title can be passed from the URL or fetched from TMDB if needed
    review, created = Review.objects.get_or_create(user=request.user, tmdb_id=tmdb_id, defaults={'movie_title': movie_title})
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
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

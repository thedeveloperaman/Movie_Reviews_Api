from reviews.models import Review

def recent_reviews(request):
    return {
        'reviews_sidebar': Review.objects.select_related('user__profile').order_by('-created_at')[:3]
    }

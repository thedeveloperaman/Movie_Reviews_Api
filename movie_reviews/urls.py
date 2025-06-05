from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('', include('core.urls')),
    path('movies/', include('movies.urls')),
    path('accounts/', include('accounts.urls')),
    path('reviews/', include('reviews.urls')),
    path('lists/', include('lists.urls')),  # <-- add this line
    path('admin/', admin.site.urls),
]


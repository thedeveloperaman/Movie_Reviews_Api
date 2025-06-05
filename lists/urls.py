from django.urls import path
from . import views

app_name = 'lists'

urlpatterns = [
    path('my-lists/', views.my_lists_view, name='my-lists'),
    path('list/<int:list_id>/', views.list_detail_view, name='list-detail'),
    path('list/<int:list_id>/delete/<int:item_id>/', views.delete_movie_from_list, name='delete-movie'),
    path('create/', views.create_list_view, name='create-list'),
    path('add-movie/<int:list_id>/', views.add_movie_to_list, name='add-movie'),
    path('edit/<int:list_id>/', views.edit_list_view, name='edit-list'),
    path('delete/<int:list_id>/', views.delete_list_view, name='delete-list'),
]

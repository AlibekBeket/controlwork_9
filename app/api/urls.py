from django.urls import path

from api.views import favorite_add_view, favorite_delete_view, get_token_view

urlpatterns = [
    path('token/', get_token_view, name='token'),
    path('favorite_add/<int:pk>/', favorite_add_view, name='api_favorite_add'),
    path('favorite_delete/<int:pk>/', favorite_add_view, name='api_favorite_delete'),
]

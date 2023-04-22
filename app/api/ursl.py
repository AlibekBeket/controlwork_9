from django.urls import path

from api.views import FavoriteAddView, FavoriteDeleteView

urlpatterns = [
    path('favorite_add/<int:pk>/', FavoriteAddView.as_view(), name='api_favorite_add'),
    path('favorite_delete/<int:pk>/', FavoriteDeleteView.as_view(), name='api_favorite_delete'),
]

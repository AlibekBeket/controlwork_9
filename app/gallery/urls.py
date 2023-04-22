from django.urls import path

from gallery.views.gallery import GalleryListView, PhotoAddView, PhotoDetailView

urlpatterns = [
    path('', GalleryListView.as_view()),
    path('gallery/', GalleryListView.as_view(), name='gallery_list'),
    path('photo_create/', PhotoAddView.as_view(), name='photo_create'),
    path('photo_detail/', PhotoDetailView.as_view(), name='photo_detail'),
]

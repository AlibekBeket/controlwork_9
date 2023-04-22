from django.urls import path

from gallery.views.gallery import GalleryListView, PhotoAddView, PhotoDetailView, PhotoUpdateView, PhotoDeleteView

urlpatterns = [
    path('', GalleryListView.as_view()),
    path('gallery/', GalleryListView.as_view(), name='gallery_list'),
    path('photo_create/', PhotoAddView.as_view(), name='photo_create'),
    path('photo_detail/<int:pk>', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo_update/<int:pk>', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo_delete/<int:pk>', PhotoDeleteView.as_view(), name='photo_delete'),
]

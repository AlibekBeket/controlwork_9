from django.urls import path

from gallery.views.gallery import GalleryListView

urlpatterns = [
    path('', GalleryListView.as_view()),
    path('gallery/', GalleryListView.as_view(), name='gallery_list'),
]

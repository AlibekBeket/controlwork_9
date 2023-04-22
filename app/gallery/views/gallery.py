from django.views.generic import ListView

from gallery.models import Photo


class GalleryListView(ListView):
    template_name = 'gallery_list.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ('created_at',)

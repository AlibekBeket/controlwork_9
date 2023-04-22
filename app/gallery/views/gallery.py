from django.views.generic import ListView

from gallery.models.photo import Photo


class PostsListView(ListView):
    template_name = 'gallery_list.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ('created_at',)

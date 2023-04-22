from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView

from gallery.models import Photo

from gallery.forms import PhotoForm


class GalleryListView(ListView):
    template_name = 'gallery_list.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ('created_at',)


class PhotoAddView(CreateView):
    template_name = 'photo_create.html'
    model = Photo
    form_class = PhotoForm

    def get_success_url(self):
        return reverse('gallery_list')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = self.request.user
            signature = form.cleaned_data.get('signature')
            photo = form.cleaned_data.get('photo')
            Photo.objects.create(author=user, signature=signature, photo=photo)
            return redirect(reverse('gallery_list'))
        return render(request, 'photo_create.html',
                      context={'form': form})

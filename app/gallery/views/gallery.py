from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from gallery.models import Photo

from gallery.forms import PhotoForm


class GalleryListView(ListView):
    template_name = 'gallery_list.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ('-created_at',)


class PhotoAddView(LoginRequiredMixin, CreateView):
    template_name = 'photo_create.html'
    model = Photo
    form_class = PhotoForm
    permission_required = 'gallery.photo_add'

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


class PhotoDetailView(DetailView):
    template_name = 'photo_detail.html'
    model = Photo
    context_object_name = 'photo'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['in_favorites'] = Photo.objects.get(id=self.kwargs['pk']).favorites.all()
        print(context.get('in_favorites'))
        return context


class PhotoUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    template_name = 'photo_update.html'
    form_class = PhotoForm
    model = Photo
    groups = ['moderator']
    permission_required = 'gallery.photo_update_or_delete'

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists() or self.request.user == Photo.objects.get(
            id=self.kwargs['pk']).author


class PhotoDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    template_name = 'photo_delete.html'
    model = Photo
    groups = ['moderator']
    permission_required = 'gallery.photo_update_or_delete'

    def get_success_url(self):
        return reverse('gallery_list')

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists() or self.request.user == Photo.objects.get(
            id=self.kwargs['pk']).author

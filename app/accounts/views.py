from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from accounts.forms import LoginForm, CustomUserCreationForm, UpdateUserForm

from gallery.models import Photo


# Create your views here.
class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context=context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('login')
        login(request, user)
        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('gallery_list')


def logout_view(request):
    logout(request)
    return redirect('gallery_list')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


class UserDetailView(DetailView):
    template_name = 'user_page.html'
    model = get_user_model()
    context_object_name = 'user'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        photos = Photo.objects.all()
        user_photos = []
        for photo in photos:
            if User.objects.get(id=self.kwargs['pk']) in photo.favorites.all():
                user_photos.append(photo)
        context['photos'] = user_photos
        return context


class UpdateUserView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    template_name = 'user_update.html'
    form_class = UpdateUserForm
    model = User
    permission_required = 'accounts.update_user'

    def get_success_url(self):
        return reverse('user_profile', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user == User.objects.get(id=self.kwargs['pk'])

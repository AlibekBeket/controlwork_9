from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, UserDetailView, UpdateUserView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user_profile/<int:pk>', UserDetailView.as_view(), name='user_profile'),
    path('user_update/<int:pk>', UpdateUserView.as_view(), name='user_update'),
]

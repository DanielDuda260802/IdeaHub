from django.urls import path
from .views import UserRegistrationView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView
from . import views

app_name = 'LoginApp'  # here for namespacing of urls.

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
    path('password_success', views.Password_success, name='password_success'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name='show_profile'),
    path('<int:pk>/edit_profile', EditProfilePageView.as_view(), name='edit_profile_page')
]
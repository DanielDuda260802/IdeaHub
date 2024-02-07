from django.urls import path
from .views import UserRegistrationView, UserEditView

app_name = 'LoginApp'  # here for namespacing of urls.

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name='register'),
    path('edit_profile', UserEditView.as_view(), name='edit_profile'),
]
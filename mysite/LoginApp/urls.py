from django.urls import path
from .views import UserRegistrationView

app_name = 'LoginApp'  # here for namespacing of urls.

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name='register'),
    
]
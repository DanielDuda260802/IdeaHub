from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from django.views.generic import DetailView, UpdateView, CreateView
from IdeaHub.models import Profile

# Create your views here.
class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('IdeaHub:homepage')

    def get_object(self):
        return self.request.user
    
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('loginapp:password_success')

def Password_success(request):
    return render(request, 'registration/password_success.html')

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context
    
class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_picture', 'website_url', 'facebook_url', 'instagram_url', 'github_url']
    success_url = reverse_lazy('IdeaHub:homepage')

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile.html'

    # making user ID available to profile 
    # save form --> gets saved under the right user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
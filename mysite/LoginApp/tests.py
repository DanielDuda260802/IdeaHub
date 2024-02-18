from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from LoginApp import views
from .views import UserRegistrationView, UserEditView, PasswordsChangeView, Password_success, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth.models import User
from IdeaHub.models import Profile

# Create your tests here.
class LoginAppTestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('loginapp:register')
        self.assertEquals(resolve(url).func.view_class, UserRegistrationView)

    def test_edit_profile_url_is_resolved(self):
        url = reverse('loginapp:edit_profile')
        self.assertEquals(resolve(url).func.view_class, UserEditView)

    def test_change_password_url_is_resolved(self):
        url = reverse('loginapp:change_password')
        self.assertEquals(resolve(url).func.view_class, PasswordsChangeView)

    def test_password_success_url_is_resolved(self):
        url = reverse('loginapp:password_success')
        self.assertEquals(resolve(url).func, views.Password_success)

    def test_show_profile_url_is_resolved(self):
        # Assuming `pk` is a placeholder for user id, we need to provide an example id.
        url = reverse('loginapp:show_profile', args=[1])
        self.assertEquals(resolve(url).func.view_class, ShowProfilePageView)

    def test_edit_profile_page_url_is_resolved(self):
        # Same here, provide an example `pk` value.
        url = reverse('loginapp:edit_profile_page', args=[1])
        self.assertEquals(resolve(url).func.view_class, EditProfilePageView)

    def test_create_profile_url_is_resolved(self):
        url = reverse('loginapp:create_profile')
        self.assertEquals(resolve(url).func.view_class, CreateProfilePageView)

class LoginAppTestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('loginapp:register')
        self.edit_profile_url = reverse('loginapp:edit_profile')
        self.change_password_url = reverse('loginapp:change_password')
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, bio='Test Bio')

    def test_UserRegistrationView_GET(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_UserEditView_GET(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.edit_profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/edit_settings.html')

    def test_PasswordsChangeView_GET(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.change_password_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/change_password.html')

    def test_ShowProfilePageView_GET(self):
        # Assuming URL pattern for profile view uses user's ID
        profile_url = reverse('loginapp:show_profile', args=[self.user.profile.id])
        response = self.client.get(profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/user_profile.html')

    def test_EditProfilePageView_GET(self):

        self.client.login(username='testuser', password='12345')
        edit_profile_page_url = reverse('loginapp:edit_profile_page', args=[self.profile.id])
        response = self.client.get(edit_profile_page_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/edit_profile_page.html')


    def test_CreateProfilePageView_GET(self):
        self.client.login(username='testuser', password='12345')
        create_profile_url = reverse('loginapp:create_profile')  # Adjust if necessary
        response = self.client.get(create_profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/create_profile.html')

    def tearDown(self):
        # Clean up after each test
        self.user.delete()

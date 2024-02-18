import factory
from django.contrib.auth.models import User
from .models import Post, Category, Profile, Comment
import random

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        password = extracted if extracted else factory.Faker('password').evaluate(None, None, extra={'locale': None})
        self.set_password(password)

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')

class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    bio = factory.Faker('text')
    website_url = factory.Faker('url')
    facebook_url = factory.Faker('url')
    instagram_url = factory.Faker('url')
    github_url = factory.Faker('url')

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence')
    title_tag = "IdeaHub"
    header_image = None  # Ako nemate default sliku
    author = factory.SubFactory(UserFactory)
    body = factory.Faker('text')
    category = factory.SubFactory(CategoryFactory)
    

class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    post = factory.SubFactory(PostFactory)
    comment_author = factory.SubFactory(UserFactory)
    body = factory.Faker('text', max_nb_chars=200)
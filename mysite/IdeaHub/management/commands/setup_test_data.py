import random

from django.db import transaction
from django.core.management.base import BaseCommand

from IdeaHub.models import User, Post, Category, Profile
from IdeaHub.factory import UserFactory, CategoryFactory, ProfileFactory, PostFactory, CommentFactory

NUM_USERS = 5
NUM_CATEGORIES = 10
NUM_POSTS = 100
NUM_COMMENTS = 200

admin_username = 'DanielD'

class Command(BaseCommand):
    help = "Generates test data for IdeaHub."

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")

        users_to_delete = User.objects.exclude(username=admin_username)
        Profile.objects.filter(user__in=users_to_delete).delete()
        Post.objects.filter(author__in=users_to_delete).delete()
        users_to_delete.delete()
        Category.objects.all().delete()

        self.stdout.write("Creating new data...")

        users = [UserFactory() for _ in range(NUM_USERS)]
        categories = [CategoryFactory() for _ in range(NUM_CATEGORIES)]

        for user in users:
            ProfileFactory(user=user)  # Assuming each user should have one profile

        for _ in range(NUM_POSTS):
            PostFactory(author=random.choice(users), category=random.choice(categories))

        posts = [PostFactory(author=random.choice(users), category=random.choice(categories)) for _ in range(NUM_POSTS)]

        for _ in range(NUM_COMMENTS):
            CommentFactory(
                post=random.choice(posts),
                comment_author=random.choice(users)
            )
        
        # Add likes to posts
        for post in posts:
            likers = random.sample(users, k=random.randint(0, NUM_USERS))  # Select random users to like the post
            post.likes.set(likers)  # Set the likes for the post

        self.stdout.write(f"Created {NUM_USERS} users, {NUM_CATEGORIES} categories, {NUM_POSTS} posts, and {NUM_COMMENTS} comments.")

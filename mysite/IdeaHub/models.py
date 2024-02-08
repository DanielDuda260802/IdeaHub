from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="IdeaHub")
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='undefined')
    likes = models.ManyToManyField(User, related_name="blog_posts") # ManyToMany --> post_id + user_id

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '(' + str(self.author) + ')'
    
    def get_absolute_url(self):
        #return reverse('IdeaHub:idea_detail', args=(str(self.id)))
        return reverse('IdeaHub:homepage')
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()  
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('IdeaHub:homepage')
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)
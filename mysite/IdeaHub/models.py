from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="IdeaHub")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='undefined')

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
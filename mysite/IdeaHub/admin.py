from django.contrib import admin
from .models import *

# Register your models here.
models_list = [UserProfile, Idea, Rating, Comment, Team, Project]
admin.site.register(models_list)
from django.contrib import admin
from .models import *

# Register your models here.
models_list = [Post, Category]
admin.site.register(models_list)
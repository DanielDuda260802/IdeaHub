from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

## Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class IdeaDetailView(DetailView):
    model = Post
    template_name = 'idea_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def get_context_data(self, *args, **kwargs ):
        category_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context 

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html' 
    fields = '__all__'

    def get_context_data(self, *args, **kwargs ):
        category_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

    def get_context_data(self, *args, **kwargs ):
        category_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('IdeaHub:homepage')

    def get_context_data(self, *args, **kwargs ):
        category_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

def CategoryView(request, categories):
    category_post = Post.objects.filter(category=categories.replace('-', ' '))
    return render(request, 'category.html', {'categories':categories.title().replace('-', ' '), 'category_post':category_post})


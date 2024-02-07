from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup

## Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class IdeaDetailView(DetailView):
    model = Post
    template_name = 'idea_details.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(IdeaDetailView, self).get_context_data() 
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()  # total_likes --> function from models
        
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    
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

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id')) # post_id --> like button name
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('IdeaHub:idea_detail', args=[str(pk)]))
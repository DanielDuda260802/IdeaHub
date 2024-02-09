from django.urls import path
from . import views
from .views import HomeView, IdeaDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView, AddComment,UpdateCommentView,DeleteCommentView

app_name = 'IdeaHub'  # here for namespacing of urls.

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('ideja/<int:pk>', IdeaDetailView.as_view(), name='idea_detail'),
    path('addPost/', AddPostView.as_view(), name='add_post'),
    path('updatePost/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('deletePost/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('addCategory/', AddCategoryView.as_view(), name='add_category'),
    path('kategorija/<str:categories>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('ideja/<int:pk>/comment', AddComment.as_view(), name='add_comment'),
    path('updateComment/<int:pk>', UpdateCommentView.as_view(), name='update_comment'),
    path('deleteComment/<int:pk>', DeleteCommentView.as_view(), name='delete_comment'),
]
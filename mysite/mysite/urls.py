from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('', include('IdeaHub.urls')), 
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), #Django Authentication system --> automatski upravlja svim url-ovima potrebnim za Login (Login page, Logout, Registation page...)
    path('login/', include('LoginApp.urls')),
    path('<int:uid>/', include('LoginApp.urls')),
]
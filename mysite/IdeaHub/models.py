from django.db import models
from django.contrib.auth.models import User

"""
Povezan sa ugrađenim Django modelom user koji sadrži polja: username, first_name, last_name, email, password, groups, user_permissions, is_staff, is_active,
is_superuser, last_login, data_joined i atribute: is_authenticated, is_anonymous te određene metode
"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username

"""
Svaka ideja sadrži naslov, opis, a može sadržavati i sliku, te atribute: datum stvaranja i autor, a dodatno sadrži i atribute:
category --> Polje koje predstavlja kategoriju kojoj ideja pripada.
status -->  Primjerice, može biti "Ongoing" (u tijeku), "Completed" (završeno) ili bilo koji drugi status
views --> broj pregleda ideje/objave
likes --> broj sviđanja ideje/objave
"""
class Idea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='idea_images/', blank=True, null=True)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Ongoing') 
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
"""
Ocjena određene ideje koja sadrži atribute:
idea --> Povezano s modelom Idea putem ForeignKey iz razloga što se svaka ocjena odnosi na određenu ideju
user --> Povezano s ugrađenim Django modelom User putem ForeignKey jer svaku ocjenu daje određeni korisnik
rating --> Brojčano polje koje predstavlja ocjenu koju je korisnik dao ideji
"""
class Rating(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.idea.title} - {self.rating}"
    
"""
Svaki korisnik može komentirati određenu ideju što je omogućeno modelom Comment:
idea --> koju ideju komentira
user --> koji korisnik komentira
text --> što komentira
created_at --> kada komentira   
"""
class Comment(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.idea.title} - {self.created_at}"
    
"""
Kako bi omogućili suradnju u radu na ideji, potrebni su nam slijedeći modeli:
Team - Udruženi korisnici koji rade na nekoj ideji
     - name --> ime tima, leader --> vođa tima, members --> članovi tima
Project - Projekt(Ostvarivanje neke ideje) na kojemu radi određeni tim
        - name --> ime projekta, team --> tim koji radi na projektu, ideas --> na kojoj ideji rade
"""
class Team(models.Model):
    name = models.CharField(max_length=255)
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leading_team')
    members = models.ManyToManyField(User, related_name='teams')

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    ideas = models.ManyToManyField('Idea', related_name='projects')

    def __str__(self):
        return self.name

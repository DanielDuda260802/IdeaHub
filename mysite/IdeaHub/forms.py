from django import forms
from .models import Post, Category, Comment
from django.utils import timezone

choices = Category.objects.all().values_list('name', 'name')
choice_list = [(choice[0], choice[1].title()) for choice in choices]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'header_image' )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title here'}), # form-control --> Bootstrap item
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title tag here'}),
            # 'value' --> whatever our Javascript has told it to be
            # 'id':'user' --> allows writing JavaScript files
            # 'type':'hidden' --> make TextInput hidden so users can't change the post's author
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'user', 'type':'hidden'}),  
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control custom-select'}),
            'body': forms.HiddenInput(),
            'header_image': forms.FileInput(attrs={'class': 'form-control-file'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), # form-control --> Bootstrap item
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.HiddenInput()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',) 

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        comment = super().save(commit=False)
        # Postavljamo date_added na trenutni datum i vrijeme
        comment.date_added = timezone.now()
        if commit:
            comment.save()
        return comment
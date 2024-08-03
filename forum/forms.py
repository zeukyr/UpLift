from django import forms
from .models import Post, Comment

choices = [("Social", "Social"), ("Advice", "Advice"), ("Resources", "Resources")]

class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "category", "body")
        widgets = {
            "title": forms.TextInput(attrs={}),
            "author": forms.TextInput(attrs={"value": "", "id":"uname", "type": "hidden"}),
            "category": forms.Select(choices=choices, attrs={}),
            "body": forms.Textarea(attrs={}),
        }

class postComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body")
        widgets = {
            "name": forms.TextInput(attrs={}),
            "body": forms.Textarea(attrs={}),
        }
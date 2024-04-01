# app/forms.py
from django import forms
from .models import Tweet, Post, Thread
from django.forms import ModelForm

class ThreadForm(forms.Form):
    title = forms.CharField(max_length=255)

class PostForm(forms.Form):
    user_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)

class TweetForm(forms.Form):
    message = forms.CharField(max_length=255, required=True)
    point = forms.IntegerField(required=True)
    name = forms.CharField(max_length=50, required=True)

class ThreadPostForm(ModelForm):
    class Meta:
        model = Thread
        fields =['title']
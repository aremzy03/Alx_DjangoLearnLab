from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = ['name']
# TagWidget() ('tags', 'widgets')

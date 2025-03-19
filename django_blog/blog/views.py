from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
# Create your views here.

# Home View


def home(request):
    return render(request, 'blog/index.html')


# Authentication Views
class UserRegister(CreateView):
    form_class = UserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('create-profile')


# class UpdateProfile(LoginRequiredMixin):
#     template_name = 'blog/profile.html'
#     class Meta:
#         model = UserProfile
#         fields = ['email', 'profile', 'bio']

class UserLogin(LoginView):
    template_name = 'blog/login.html'
    success_url = reverse_lazy('viewprofile')
    next_page = success_url

class UserLogout(LogoutView):
    template_name = 'blog/logout.html'
    success_url = reverse_lazy('home')
    #next_page = success_url

class CreateProfile(LoginRequiredMixin, CreateView):
    model = UserProfile
    template_name = 'blog/createprofile.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = "blog/updateprofile.html"
    fields = ['name', 'email', 'profileimg', 'bio']
    def get_success_url(self):
        if self.request.user.userprofile:
            return reverse_lazy('viewprofile')
        else:
            return reverse_lazy('create-profile')

    def get_object(self, queryset=None):
        return self.request.user.userprofile
    #POST method save()

@login_required
def viewprofile(request):
    userp = request.user
    if not userp.is_authenticated:
        raise PermissionError
    else:
        profile = UserProfile.objects.get(user=userp)
        context = {'name': profile.name, 'bio': profile.bio,
                   'profilepic': profile.profileimg}
        template = 'blog/profile.html'
        return render(request, template, context)

# Post Views


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    fields = ['title', 'content', 'author']
    success_url = reverse_lazy('home')


class ListPost(ListView):
    model = Post
    template_name = 'blog/list_post.html'
    context_object_name = 'posts'


class DetailPost(DetailView):
    model = Post
    template_name = 'blog/detail_post.html'
    context_object_name = 'post'


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('home')

    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/deletepost.html'
    success_url = reverse_lazy('home')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

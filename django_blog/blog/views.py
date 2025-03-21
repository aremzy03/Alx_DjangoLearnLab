from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse, reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

# Home View


def home(request):
    return render(request, 'blog/index.html')


# Authentication Views
class UserRegister(CreateView):
    form_class = UserCreationForm
    template_name = 'blog/register.html'

    def get_success_url(self):
        return reverse_lazy('create-profile')


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
    # next_page = success_url


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
    # POST method save()


@login_required(login_url=reverse_lazy('login'))
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
    login_url = reverse_lazy('login')
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'author']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        form.save_m2m()
        return super().form_valid(form)


@login_required(login_url=reverse_lazy('login'))
def createpost(request):
    post = Post.objects.create()
    template = 'blog/post_form.html'
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail-post', pk=post.pk)
    else:
        form = PostForm()
    context = {'post': post, 'form': form}
    return render(request, template, context)


class ListPost(ListView):
    model = Post
    template_name = 'blog/list_post.html'
    context_object_name = 'posts'


class PostByTagListPost(ListView):
    model = Post
    template_name = 'blog/list_post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_name = self.kwargs.get('tag')
        return Post.objects.filter(tags__name__icontains=tag_name)


class DetailPost(DetailView):
    model = Post
    template_name = 'blog/detail_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post=self.get_object())
        return context


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = reverse_lazy('login')
    permission_denied_message = "You can't access this content"
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'tags']
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = reverse_lazy('login')
    permission_denied_message = "You can't access this content"
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class SearchPostList(ListPost):

    def get_queryset(self):
        search = self.request.GET.get('search')
        return Post.objects.filter(Q(tags__name__icontains=search) | Q(title__icontains=search) | Q(content__icontains=search))

# Comment Views


@login_required(login_url=reverse_lazy('login'))
def commentform(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    template = 'blog/detail_post.html'

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('detail-post', pk=post.pk)
    else:
        form = CommentForm()
    context = {'post': post, 'comments': comments, 'form': form}
    return render(request, template, context)

# def updatecomment(request, pk, pk2):
#     post = get_object_or_404(Post, pk=pk)
#     comment = get_object_or_404(Comments, pk=pk2)
#     template = 'blog/detail_post.html'

#     if request.method=='PUT':
#         form = CommentForm(request.PUT)
#         if form.is_valid:
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.author = request.user
#             comment.save()
#             return redirect('detail-post', pk=pk)
#     else:
#         form = CommentForm()
#     context = {'post':post, 'comment':comment, 'form':form}
#     return render(request, template, context)


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = "blog/comment_form.html"
    fields = ['content']
    success_url = reverse_lazy('posts')


class CommentCreateView(CreateView):
    model = Comment
    template_name = "comment_form.html"
    fields = '__all__'
    success_url = reverse_lazy('posts')


class CommentListView(ListView):
    model = Comment
    template_name = "blog/detail_post.html"
    context_object_name = 'comments'


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = "blog/delete_comment.html"
    success_url = reverse_lazy('posts')

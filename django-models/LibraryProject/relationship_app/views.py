from django.shortcuts import render #, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Permission
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Library, Book, UserProfile, Author, Librarian, User
from .signals import *

# Create your views here.


def index(request):
    return render(request, 'relationship_app/index.html')


def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             messages.error(request, 'Username or Password is incorrect')
#     return render(request, 'login.html')

# def logout_view(request):
#     logout(request)
#     messages.success(request, 'You have been logged out')
#     return redirect(login_view)
        
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context


class RegisterUserView(CreateView):
    form_class = UserCreationForm()
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

# class Login_view(LoginView):
#     template_name = 'relationship_app/login.html'
    
#     def get_success_url(self):
#         return reverse_lazy('index')

# class Logout_view(LogoutView):
#     template_name = 'relationship_app/logout.html'

def is_admin(user):
    if user.role == 'admin':
        return

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("This is an admin View")

def is_librarian(user):
    if user.role == 'librarian':
        return

@user_passes_test(is_librarian)
def librarian_view(user):
    return HttpResponse("This is a Librarian View")

def assign_permissions_add():
    user = User.objects.get(username="admin")
    permission = Permission.objects.get(codename='can_add_book')
    user.user_permissions.add(permission)

def assign_permissions_change():
    user = User.objects.get(username="admin")
    permission = Permission.objects.get(codename='can_change_book')
    user.user_permissions.add(permission)

def assign_permissions_delete():
    user = User.objects.get(username="admin")
    permission = Permission.objects.get(codename='can_delete_book')
    user.user_permissions.add(permission)

@permission_required("relationship_app.can_add_book", raise_exception=True)
def create_book(request):
    author = Author.objects.create(name="New Author")
    book = Book.objects.create(title="New Book", author=author)
    library = Library.objects.get(name="Abuja")
    library.books.add(book)
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

@permission_required("relationship_app.can_change_book", raise_exception=True)
def change_book(request):
    book = Book.objects.get(title="")
    book.title = ""
    book.save()
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request):
    book = Book.objects.get(title="")
    if book:
        book.delete()
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)
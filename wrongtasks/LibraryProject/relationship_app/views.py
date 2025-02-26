from django.shortcuts import render #, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Permission, Group
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Library, Book, Author, CustomUser
from .signals import *

# Create your views here.


def index(request):
    return render(request, 'relationship_app/index.html')


def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)
        
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context


class RegisterUserView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'admin'

@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'librarian'

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'member'

@user_passes_test(is_librarian, login_url='/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

def assign_permissions_add():
    user = CustomUser.objects.get(username="admin")
    permission = Permission.objects.get(codename='can_add_book')
    user.user_permissions.add(permission)

def assign_permissions_change():
    user = CustomUser.objects.get(username="admin")
    permission = Permission.objects.get(codename='can_change_book')
    user.user_permissions.add(permission)

def assign_permissions_delete():
    user = CustomUser.objects.get(username="admin")
    permission = Permission.objects.get(codename='can_delete_book')
    user.user_permissions.add(permission)

"""
Creating Groups and Assingning Permissions
The following code snippet creates three groups: Editors, Viewers, and Admins.
The Editors group has the permissions to view, change, and edit books using the can_view, can_change, and can_edit code_names.
The Viewers group only has the permission to view books using the can_view codename.
The Admins group has all the permissions.
The code snippet assigns the permissions to the groups.

"""
# Create groups
editor, created = Group.objects.get_or_create(name='Editors')
viewer, created = Group.objects.get_or_create(name='Viewers')
admin, created = Group.objects.get_or_create(name='Admins')
# Assign permissions to groups
#editor
permissions_editor = Permission.objects.filter(codename__in=['can_view', 'can_change', 'can_edit'])
editor.permissions.add(*permissions_editor)
#viewer
permissions_viewer = Permission.objects.filter(codename__in=['can_view'])
viewer.permissions.add(*permissions_viewer)
#Admin
permissions_admin = Permission.objects.all()
admin.permissions.add(*permissions_admin)

@permission_required("relationship_app.can_create", raise_exception=True)
def create_book(request):
    author = Author.objects.create(name="New Author")
    book = Book.objects.create(title="New Book", author=author)
    library = Library.objects.get(name="Abuja")
    library.books.add(book)
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

@permission_required("relationship_app.can_change", raise_exception=True)
def change_book(request):
    book = Book.objects.get(title="")
    book.title = ""
    book.save()
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

@permission_required("relationship_app.can_delete", raise_exception=True)
def delete_book(request):
    book = Book.objects.get(id=10)
    if book:
        book.delete()
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

@permission_required("relationship_app.can_view", raise_exception=True)
def view_book(request):
    book = Book.objects.get(id=3)
    # context = {'book': book}
    # return render(request, 'relationship_app/list_books.html', context)
    return HttpResponse(book)

@permission_required("relationship_app.can_edit", raise_exception=True)
def edit_book(request):
    book = Book.objects.get(title="book1")
    book.title = "book2"
    book.author = Author.objects.get(name="first author")
    book.save()
    return HttpResponse(book)
    
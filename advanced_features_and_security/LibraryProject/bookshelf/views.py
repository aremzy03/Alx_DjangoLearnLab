from django.shortcuts import render
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Book, CustomUser

# Create your views here.
"""
Creating Groups and Assingning Permissions
The following code snippet creates three groups: Editors, Viewers, and Admins.
The Editors group has the permissions to view, change, and edit books using the can_view, can_change, and can_edit code_names.
The Viewers group only has the permission to view books using the can_view codename.
The Admins group has all the permissions.
The code snippet assigns the permissions to the groups.

"""
# Create groups
def assign_permissions(request):
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
	return HttpResponse("Permissions assigned successfully")

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request):
    book = Book.objects.get(title="")
    return HttpResponse(book)

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
	book = Book.objects.create(title="", author="", publication_year="")
	return HttpResponse(book)

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request):
	book = Book.objects.get(title="")
	book.title = ""
	book.author = ""
	book.publication_year = ""
	book.save()
	return HttpResponse(book)

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request):
	book = Book.objects.get(title="")
	book.delete()
	return HttpResponse(book)

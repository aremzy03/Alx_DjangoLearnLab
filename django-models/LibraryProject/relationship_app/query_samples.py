from .models import *
library_name = ''
library = Library.objects.get(name=library_name)
library.books.all()

author_name = ''
author = Author.objects.get(author = author_name)
Book.objects.filter(author=author)

librarian = Librarian.objects.get(library =library_name)

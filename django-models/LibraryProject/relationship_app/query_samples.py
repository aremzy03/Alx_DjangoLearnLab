from .models import *



def retrieve_book():
    author = input("Who's Books do you want to read?")
    Book.objects.get(author = author)

def retrieve_Library():
    Library.objects.all()

def get_librarian():
    library_name = input("What Librarian are you looking for?")
    Librarian.objects.get(library =library_name)

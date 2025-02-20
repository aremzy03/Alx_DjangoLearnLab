from django.shortcuts import render
from django.views.generic import DetailView
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def display_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book_list.html', context)

class Librarybook(DetailView):
    model = Library
    template_name = 'library_book.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
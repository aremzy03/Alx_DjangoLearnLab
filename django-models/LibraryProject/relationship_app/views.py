from django.shortcuts import render #, redirect
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .models import *

# Create your views here.


def index(request):
    return render(request, 'index.html')


def display_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book_list.html', context)

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
        
class Librarybook(DetailView):
    model = Library
    template_name = 'library_book.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context


class RegisterUserView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class Login_view(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('index')

class Logout_view(LogoutView):
    template_name = 'logout.html'

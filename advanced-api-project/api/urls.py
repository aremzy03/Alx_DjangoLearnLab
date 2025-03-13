from django.urls import path
from .views import *

urlpatterns = [
	path('books/', ListView.as_view(), name='book-list'),
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update'),
    path('books/create/', CreateView.as_view(), name='book-create'),
    path('books/delete/', DeleteView.as_view(), name='book-delete'),
]


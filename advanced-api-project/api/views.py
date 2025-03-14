from django.forms import ValidationError
from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


"""_summary_

    Raises:
        ValidationError: 
        ValidationError: 

    Returns:
"""
# Create your views here.
class ListView(mixins.ListModelMixin, generics.GenericAPIView):
    """This view displays the list of books in the database in json format

    Args:
        mixins (class): 
        generics (class): 

    Returns:
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'publication_year', 'author']
    search_fileds = ['title', 'author']
    ordering_fields = ['title', 'publication_year', 'author']
       
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class DetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """This view displays the details of a book in the database in json format

    Args:
        mixins (class): 
        generics (class): 

    Returns:
        _type_: 
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class CreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    """This view creates a new book in the database

    Args:
        mixins (class): 
        generics (class): 

    Raises:
        ValidationError: 

    Returns:
        _type_: 
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        if not serializer.is_valid():
            raise ValidationError("Invalid data")
        serializer.save()

class UpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    """This view updates the details of a book in the database

    Args:
        mixins (class): 
        generics (class):

    Raises:
        ValidationError: 

    Returns:
        _type_: 
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        if not serializer.is_valid():
            raise ValidationError("Invalid data")
        serializer.save()

class DeleteView(mixins.DestroyModelMixin, generics.GenericAPIView):
    """This view deletes a book from the database

    Args:
        mixins (class): 
        generics (class): 

    Returns:
        _type_: 
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'title'
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
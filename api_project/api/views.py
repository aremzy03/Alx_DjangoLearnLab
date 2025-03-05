from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serilizers import Book, BookSerializer

# Create your views here.


class BookList(generics.ListAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)

        

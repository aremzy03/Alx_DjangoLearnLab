from django.test import TestCase
from .models import Author, Book
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
# Testing Models.
class AuthorModelTest(TestCase):
    """Test module for Author model"""

    def setUp(self):
        Author.objects.create(name='Mustapha Aremu')

    def test_author_name(self):
        author = Author.objects.get(name='Mustapha Aremu')
        self.assertEqual(author.name, 'Mustapha Aremu')

    def test_author_str(self):
        author = Author.objects.get(name='Mustapha Aremu')
        self.assertEqual(str(author), 'Mustapha Aremu')

class BookModelTest(TestCase):
    """Test module for Book model"""
    
    def setUp(self):
        self.author = Author.objects.create(name='Mustapha Aremu')
        self.book = Book.objects.create(title='The Book', publication_year=2020, author=self.author)
        
    def test_book_title(self):
        book = Book.objects.get(title='The Book')
        self.assertEqual(book.title, 'The Book')

    def test_book_publication_year(self):
        book = Book.objects.get(title='The Book')
        self.assertEqual(book.publication_year, 2020)

    def test_book_author(self):
        book = Book.objects.get(title='The Book')
        self.assertEqual(book.author.name, 'Mustapha Aremu')

    def test_book_str(self):
        book = Book.objects.get(title='The Book')
        self.assertEqual(str(book), 'The Book by Mustapha Aremu')

#Testing Views
class TestViews(APITestCase):
    def setUp(self):
        
        self.author = Author.objects.create(name='Mustapha Aremu')
        self.book = Book.objects.create(title='The Book', publication_year=2020, author=self.author)

    def test_list_view(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        url = reverse('book-detail', kwargs={'pk': self.book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_view(self):
        url = reverse('book-create')
        data = {'title': 'The Book', 'publication_year': 2020, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_view(self):
        url = reverse('book-update', kwargs={'pk': self.book.id})
        data =  {'title': 'The Book', 'publication_year': 2020, 'author': self.author.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_view(self):
        url = reverse('book-delete', kwargs={'title': self.book.title})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    
#forcing authentication to test views that needs authentication   
class TestViewsAuth(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='user123')
        self.author = Author.objects.create(name='Mustapha Aremu')
        self.book = Book.objects.create(title='The Book', publication_year=2020, author=self.author)
        
    def test_create_view_auth(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('book-create')
        data = {
                'title': 'The Book',
                'publication_year': 2020,
                'author': self.author.id
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_update_view_auth(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('book-update', kwargs={'pk': self.book.id})
        data = {
                'title': 'The Book',
                'publication_year': 2020,
                'author': self.author.id
                }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_detail_view_auth(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('book-detail', kwargs={'pk': self.book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
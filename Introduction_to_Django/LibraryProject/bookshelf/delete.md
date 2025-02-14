from bookshelf.models import book
book = Book.objects.get(title= "1984")
book.delete()
from bookshelf.model import book
book = Book.objects.get(title= "1984")
book.delete()
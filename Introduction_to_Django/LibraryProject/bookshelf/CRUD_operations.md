## Create Book
from bookshielf.models import Book

Book.objects.create(title= "1984", author= "George Orwell", publication_year= 1949)

output: <Book: 1984 by George Orwell (1949)>

## Retrieve Book
Book.objects.get(title="1984")

output: <Book: 1984 by George Orwell (1949)>

## Update Book
book = Book.objects.get(id=1)

book.title = "Nineteen Eighty-Four"

book.save()

Book.objects.all()

output: <QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>

## Delete Book
Book.objects.filter(id=1).delete()

output: (0, {})

Book.objects.all()

output: <QuerySet []>

## Exit shell
exit()
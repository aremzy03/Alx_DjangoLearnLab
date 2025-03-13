from django.db import models

# Create your models here.
"""
	The Author model is a data table with the author's name as the only record
	The Book model is table with 3 records: title, publication_year 
 	and the author (which is a foreignkey to the Book model) 
"""

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} by {self.author}"

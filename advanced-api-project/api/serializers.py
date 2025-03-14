from rest_framework import serializers
from .models import Author, Book
from datetime import datetime, date

"""_summary_

	AuthorSerialiszer and BookSerializer takes the author and Book models to convert them to
	json data
 	
	BookSerilizer.validate:
		checks if the publication year of the book is valid
    Raises:
		serializers.ValidationError: raises an error when publication year is in the future

	Returns:
		list: list of the data model fields
"""

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']
    
class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']
        
    def validate(self, data):
        year = date.today().year
        publication_year = data.get('publication_year')
        if publication_year and publication_year > year:
            raise serializers.ValidationError("Publication year must be a valid year")
        return data
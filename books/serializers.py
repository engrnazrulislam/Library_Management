from rest_framework import serializers
from books.models import Book, Status, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title','author','category','isbn','image','created_at','updated_at','status']
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','biography']
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id','name','description']
from rest_framework import serializers
from books.models import Book, Status, Author

class BookSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2,coerce_to_string=False)
    class Meta:
        model = Book
        fields = ['id', 'title','author','category','isbn','image','added_at','updated_at','price','quantity','status']
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','biography']
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id','name','description']
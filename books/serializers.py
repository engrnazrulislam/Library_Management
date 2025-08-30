from rest_framework import serializers
from .models import Book, Author, BookImage

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography']

# ProductImageSerializer for ProductImage Model
class BookImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = BookImage
        fields = ['id','image']

class BookSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False)
    images = BookImageSerializer(many=True, read_only=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    author_name = serializers.CharField(source='author.name', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_name', 'category', 'isbn', 'image','images', 'price', 'quantity', 'added_at', 'updated_at']
    
    def create(self, validated_data):
        image = validated_data.pop('image', None)
        book = super().create(validated_data)
        if image:
            BookImage.objects.create(book=book, image=image)
        return book
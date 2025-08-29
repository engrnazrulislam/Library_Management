from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Author
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets, filters
from .models import Author
from api.permissions import IsAdminOrReadOnly

# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name', 'isbn']

class ViewSpecificBook(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'id'

    def delete(self, request, id, *args, **kwargs):
        product = get_object_or_404(Book, pk=id)
        if product.stock > 10:
            return Response({'message': 'Book with stock more then 10 could not be deleted'})
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
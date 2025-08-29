from rest_framework import viewsets, filters
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from api.permissions import IsLibrarianOrReadOnly
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsLibrarianOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name', 'isbn']

class ViewSpecificBook(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsLibrarianOrReadOnly]
    lookup_field = 'id'

    def delete(self, request, id, *args, **kwargs):
        book = get_object_or_404(Book, pk=id)
        if book.quantity and book.quantity > 10:
            return Response({'message': 'Book with stock more than 10 cannot be deleted'})
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

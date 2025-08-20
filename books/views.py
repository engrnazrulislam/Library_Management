from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Author, Status
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer, AuthorSerializer, StatusSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets, filters
from .models import Author


# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name', 'isbn']


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class ViewSpecificBook(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

    def delete(self, request, id, *args, **kwargs):
        product = get_object_or_404(Book, pk=id)
        if product.stock > 10:
            return Response({'message': 'Book with stock more then 10 could not be deleted'})
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
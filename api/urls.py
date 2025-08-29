from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from books.views import BookViewSet, AuthorViewSet
from members.views import MemberViewSet
from borrow.views import BorrowRecordViewSet

# Main routers
router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'books', BookViewSet, basename='book')
router.register(r'members', MemberViewSet, basename='member')
router.register(r'borrowrecords', BorrowRecordViewSet, basename='borrowrecord')

# Nested router: borrow records under members
member_router = routers.NestedDefaultRouter(router, r'members', lookup='member')
member_router.register(r'borrowrecords', BorrowRecordViewSet, basename='member-borrowrecords')

# Nested router: borrow records under books
book_router = routers.NestedDefaultRouter(router, r'books', lookup='book')
book_router.register(r'borrowrecords', BorrowRecordViewSet, basename='book-borrowrecords')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(member_router.urls)),
    path('', include(book_router.urls)),
]

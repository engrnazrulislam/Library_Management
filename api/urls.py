from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import AuthorViewSet, BookViewSet, StatusViewSet
from members.views import MemberViewSet
from borrow.views import BorrowRecordViewSet
router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='author')
router.register('books', BookViewSet, basename='book')
router.register('members', MemberViewSet, basename='member')
router.register('borrow-records', BorrowRecordViewSet, basename='borrow-record')
router.register(r'status', StatusViewSet, basename='status')
urlpatterns = router.urls
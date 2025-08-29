from rest_framework import serializers
from .models import BorrowReturnRecord

class BorrowRecordSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)
    class Meta:
        model = BorrowReturnRecord
        fields = ['id', 'book', 'book_title', 'member','status', 'borrow_date', 'return_date']

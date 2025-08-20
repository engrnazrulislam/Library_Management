from rest_framework import serializers
from .models import BorrowRecord

class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['id','book','member','borrow_date','return_date']
        
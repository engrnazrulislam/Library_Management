from rest_framework import serializers
from .models import BorrowReturnRecord

class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowReturnRecord
        fields = ['id','book','member','borrow_date','return_date','status']
        
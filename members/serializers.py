from rest_framework import serializers
from .models import Member
from borrow.models import BorrowReturnRecord

class MemberSerializer(serializers.ModelSerializer):
    borrowed_count = serializers.SerializerMethodField()
    returned_count = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ['id', 'user', 'membership_date', 'borrowed_count', 'returned_count']

    def get_borrowed_count(self, obj):
        return BorrowReturnRecord.objects.filter(member=obj, status='Borrowed').count()

    def get_returned_count(self, obj):
        return BorrowReturnRecord.objects.filter(member=obj, status='Return').count()

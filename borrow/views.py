from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django.utils.timezone import now
from .models import BorrowReturnRecord
from .serializers import BorrowRecordSerializer

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowReturnRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if not hasattr(self.request.user, 'member_profile'):
            raise ValidationError("You are not a member.")
        member = self.request.user.member_profile
        book = serializer.validated_data['book']

        if book.quantity is None or book.quantity <= 0:
            raise ValidationError({'error': 'Book not available for borrowing'})

        serializer.save(user=self.request.user, member=member, status='Borrowed')

        book.quantity -= 1
        book.save()

    def perform_update(self, serializer):
        instance = self.get_object()
        old_status = instance.status
        new_status = serializer.validated_data.get('status', old_status)
        book = instance.book

        if old_status != new_status:
            if new_status == 'Return' and old_status == 'Borrowed':
                book.quantity += 1
                serializer.save(return_date=now().date())
            elif new_status == 'Borrowed' and old_status == 'Return':
                if book.quantity <= 0:
                    raise ValidationError({'error': 'Book not available for borrowing'})
                book.quantity -= 1
                serializer.save()
            book.save()
        else:
            serializer.save()

        # if old_status != new_status:
        #     book = instance.book
        #     if new_status == 'Return':
        #         book.quantity += 1
        #         instance.return_date = now().date()
        #     elif new_status == 'Borrowed':
        #         if book.quantity <= 0:
        #             raise ValidationError({'error': 'Book not available for borrowing'})
        #         book.quantity -= 1
        #     book.save()
        #     instance.save()

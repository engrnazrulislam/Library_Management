from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from .models import BorrowReturnRecord
from .serializers import BorrowRecordSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowReturnRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        if book.quantity is None or book.quantity <= 0:
            raise ValidationError({'error': 'Book not available for borrowing'})

        serializer.save(user=self.request.user, status='Borrowed')

        book.quantity -= 1
        book.save()

    def perform_update(self, serializer):
        previous = self.get_object()
        new_status = serializer.validated_data.get('status', previous.status)
        book = serializer.validated_data.get('book', previous.book)

        if previous.status != 'Return' and new_status == 'Return':
            book.quantity += 1
            book.save()
            serializer.save(return_date=now().date())
        else:
            serializer.save()

    @action(detail=False, methods=['get'])
    def borrowed(self, request):
        borrowed_qs = self.queryset.filter(status='Borrowed')
        serializer = self.get_serializer(borrowed_qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def returned(self, request):
        returned_qs = self.queryset.filter(status='Return')
        serializer = self.get_serializer(returned_qs, many=True)
        return Response(serializer.data)

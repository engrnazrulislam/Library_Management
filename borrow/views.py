from rest_framework import viewsets
from .models import BorrowReturnRecord
from .serializers import BorrowRecordSerializer

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowReturnRecord.objects.all()
    serializer_class = BorrowRecordSerializer

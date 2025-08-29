from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializer
from api.permissions import IsLibrarian

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes=[IsLibrarian]

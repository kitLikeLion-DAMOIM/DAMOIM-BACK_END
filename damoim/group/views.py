from .models import Group
from .serializers import GroupSerializer,GroupListSerializer
from rest_framework import viewsets

class GroupViewSet(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer

class GroupListViewSet(viewsets.ModelViewSet):
    queryset=Group.objects.all()
    serializer_class=GroupListSerializer

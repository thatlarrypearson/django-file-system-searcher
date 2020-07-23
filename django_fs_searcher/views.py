# django_file_system_searcher/view.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
import django_filters.rest_framework
from .models import FileInfo
from .serializers import FileInfoSerializer


class FileInfoViewSet(viewsets.ModelViewSet):
    serializer_class = FileInfoSerializer
    model = FileInfo
    permission_classes = [IsAuthenticated, ]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, ]
    filterset_fields = ['file_name', 'dropbox_hash', ]
    queryset = FileInfo.objects.all()


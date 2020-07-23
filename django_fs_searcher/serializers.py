# django_file_system_searcher/serializers.py
from rest_framework import serializers
from .models import FileInfo


class FileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileInfo
        fields = [
            'id', 'hostname', 'volume', 'file_name', 'relative_path',
            'full_path', 'size', 'dropbox_hash', 'created', 'modified',
            'suffix', 'mime_type', 'mime_encoding', 'is_archive',
        ]



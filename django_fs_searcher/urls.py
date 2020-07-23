# django_file_system_searcher/urls.py
from django.urls import path
from django.views.generic import TemplateView
from .views import FileInfoViewSet

urlpatterns = [
    path('', TemplateView.as_view(template_name="fs_searcher-index.html"), name='index'),

    path('file_info/', FileInfoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('file_info/<int:pk>/', FileInfoViewSet.as_view({
                                                'get': 'retrieve',
                                                'put': 'update',
                                                'patch': 'partial_update',
                                                'delete': 'destroy',
                                            })
    ),

]

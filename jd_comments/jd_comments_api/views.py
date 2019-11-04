from .models import Comment
from rest_framework import viewsets
from jd_comments_api.serializers import UserSerializer
from rest_framework import viewsets,filters,pagination


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('-creationTime')
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('content',)

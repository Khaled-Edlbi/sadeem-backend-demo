from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

from .models import *
from .serializers import *


class PageSetPagination(PageNumberPagination):
    page_size = 12


class BooksListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BookSerializer
    pagination_class = PageSetPagination

    def get_queryset(self):
        queryset = Book.objects.all().order_by('-updated')
        search_query = self.request.query_params.get('q')

        # if search_query:
        #     queryset = queryset.filter(
        #         Q(enTitle__icontains=search_query) |
        #         Q(arTitle__icontains=search_query) |
        #         Q(enDescription__icontains=search_query) |
        #         Q(enDescription__icontains=search_query)
        #     )

        return queryset


class BookRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateAndUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

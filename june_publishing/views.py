from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

from .models import *
from .serializers import *


class PageSetPagination(PageNumberPagination):
    page_size = 12


class BookSeriesRetrieveAPIView(generics.RetrieveAPIView):
    queryset = BookSeries.objects.all()
    serializer_class = BookSeriesSerializer
    permission_classes = [AllowAny]


class BooksListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    pagination_class = PageSetPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Book.objects.all()

        sort_by = self.request.query_params.get('sortBy')
        sort_type = self.request.query_params.get('sortType')

        level_filter = self.request.query_params.get('level')
        date_filter = self.request.query_params.get('date')
        subject_filter = self.request.query_params.get('subject')

        if sort_by and sort_by != "undefined":
            queryset = queryset.order_by(
                ('-' if sort_type and sort_type != "undefined" and sort_type == 'Des' else '') + sort_by
            )
        else:
            queryset = queryset.order_by('-updated')

        if sort_type and level_filter != "undefined":
            queryset = queryset.filter(series__level__level__contains=level_filter)

        if level_filter and level_filter != "undefined":
            queryset = queryset.filter(series__level__level__contains=level_filter)

        if subject_filter and subject_filter != "undefined":
            queryset = queryset.filter(series__subject__subject__icontains=subject_filter)

        if date_filter and date_filter != "undefined":
            year = int(date_filter)
            start_date = f"{year}-01-01"
            end_date = f"{year}-12-31"
            queryset = queryset.filter(series__date__range=[start_date, end_date])

        return queryset


class BookCreateAndUpdateAPIView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    # permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

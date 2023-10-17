from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .serializers import *
from .models import *


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 20


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.order_by('id')
    serializer_class = BooksSerializer
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['genre', 'author']
    search_fields = ['title']
    pagination_class = StandardResultsSetPagination


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandardResultsSetPagination


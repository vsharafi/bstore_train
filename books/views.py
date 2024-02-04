from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from .models import Book


class BookListView(generic.ListView):
    template_name = 'books/book_list.html'
    model = Book
    context_object_name = 'books'
    def get_queryset(self):
        return Book.objects.all().order_by('title')
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views import generic
from .models import Book
from django.urls import reverse_lazy
from django.shortcuts import redirect

class BookListView(generic.ListView):
    template_name = 'books/book_list.html'
    model = Book
    context_object_name = 'books'
    # def get_queryset(self):
    #     return Book.objects.all().order_by('title')
    

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = '__all__'


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = '__all__'

    def form_valid(self, form):
        if form.has_changed():
            form.save()
            return redirect('book_detail', pk=self.object.pk)
        else:
            return redirect('book_update', pk=self.object.pk)


class BookDeletView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('home')
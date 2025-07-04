from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Books

class BookListView(ListView):
    model = Books
    template_name = 'library_manager/book_list.html' # optional / default: library/book_list.html
    #context_object_name = 'objects' # optional / default: object_list

class BookDetailView(DetailView):
    model = Books
    template_name = 'library_manager/book_detail.html'

class BookCreateView(CreateView):
    model = Books
    fields = '__all__'
    template_name = 'library_manager/book_form.html'
    success_url = reverse_lazy('library:book_list')

class BookUpdateView(UpdateView):
    model = Books
    fields = '__all__'
    template_name = 'library_manager/book_form.html'
    success_url = reverse_lazy('library:book_list')

class BookDeleteView(DeleteView):
    model = Books
    template_name = 'library_manager/book_confirm_delete.html'
    success_url = reverse_lazy('library:book_list')
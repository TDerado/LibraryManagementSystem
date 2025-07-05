from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Books
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class BookListView(LoginRequiredMixin, ListView):
    model = Books
    template_name = 'library_manager/book_list.html' # optional / default: library/book_list.html
    #context_object_name = 'objects' # optional / default: object_list

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Books
    template_name = 'library_manager/book_detail.html'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Books
    fields = '__all__'
    template_name = 'library_manager/book_form.html'
    success_url = reverse_lazy('library:book_list')

    def test_func(self):
        return self.request.is_staff

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Books
    fields = '__all__'
    template_name = 'library_manager/book_form.html'
    success_url = reverse_lazy('library:book_list')

    def test_func(self):
        return self.request.is_staff

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Books
    template_name = 'library_manager/book_confirm_delete.html'
    success_url = reverse_lazy('library:book_list')

    def test_func(self):
        return self.request.is_staff
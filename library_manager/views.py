from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Books, Members
from .serializers import BookSerializer, MemberSerializer
from .permissions import IsOwnerOrReadOnly, IsStaff
from rest_framework import viewsets, permissions, filters, mixins
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class MemberViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('title')
    serializer_class = BookSerializer

    filterset_fields = ['title', 'authors__first_name']
    search_fields = ['title', 'authors__first_name', 'publishers__publisher_name', 'genres__genre_name']
    ordering_fields = ['title', 'genres__genre_name']

    permission_classes = [permissions.IsAuthenticated, IsStaff]


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
        return self.request.user.is_staff

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Books
    template_name = 'library_manager/book_confirm_delete.html'
    success_url = reverse_lazy('library:book_list')

    def test_func(self):
        return self.request.user.is_staff
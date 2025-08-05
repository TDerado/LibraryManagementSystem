from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('create/', views.BookCreateView.as_view(), name='book_create'),
    path('health', views.HealthCheckView.as_view(), name='health_check'),
    path('<pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('<pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('<pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]
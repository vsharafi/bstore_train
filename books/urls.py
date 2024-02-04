from django.urls import path
from . import views



urlpatterns = [
    path('', views.BookListView.as_view(), name='home'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('create/', views.BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    
]
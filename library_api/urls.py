from django.contrib import admin
from django.urls import path
from books.views import books,book

urlpatterns = [
    path('api/books/', books, name='books'),
    path('api/books/<int:pk>/', book, name='book'),
    path('admin/', admin.site.urls),
]

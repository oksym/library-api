from django.contrib import admin
from django.urls import path,include
from books.views import BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register("books", BookViewSet)

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/", include(router.urls)),
    # path('api/books/', books, name='books'),
    # path('api/books/<int:pk>/', book, name='book'),
    path('admin/', admin.site.urls),
]

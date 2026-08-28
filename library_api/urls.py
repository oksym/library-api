from django.contrib import admin
from django.urls import path,include
from books.views import BookViewSet,home
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from books.views import BookViewSet, RegisterView
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView)
router = DefaultRouter()
router.register("books", BookViewSet)

urlpatterns = [
    path("", home, name="home"),
    path("api/schema/",SpectacularAPIView.as_view(),name="schema",),
    path("api/docs/",SpectacularSwaggerView.as_view(url_name="schema"),name="swagger-ui",),
    path("api/register/", RegisterView().as_view()),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/", include(router.urls)),
    # path('api/books/', books, name='books'),
    # path('api/books/<int:pk>/', book, name='book'),
    path('admin/', admin.site.urls),
]

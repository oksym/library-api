from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer,CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly,IsOwnerOrReadOnly
from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter


# @api_view(["GET", "POST"])
# def books(request):
#     if request.method=='GET':
#         books=Book.objects.all()
#         serializer=BookSerializer(books, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer=BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET','PUT','PATCH','DELETE'])
# def book(request,pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#         serializer=BookSerializer(book)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         serializer = BookSerializer(book,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'PATCH':
#         serializer = BookSerializer(book, data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class BookViewSet(ModelViewSet):
    queryset=Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAdminOrReadOnly] #custom
    permission_classes=[IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # book = serializer.save()
        # print(f"Created book: {book.title}")
        serializer.save(owner=self.request.user)


    def get_queryset(self):
        queryset = Book.objects.all()
        author = self.request.query_params.get("author")
        if author:
            queryset = queryset.filter(author_id=author)

        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(categories__id=category)
        return queryset

    @action(detail=False, methods=["GET"])
    def expensive(self, request):
        # books = Book.objects.filter(price__gt=50)
        # serializer = BookSerializer(books, many=True)
        books = self.get_queryset().filter(price__gt=100)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"])
    def categories(self, request, pk=None):
        book = self.get_object()
        serializer = CategorySerializer(book.categories.all(), many=True)
        return Response(serializer.data)

    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ["title", "description", "author__name"]
    ordering_fields = ["title", "price", "date"]

# @api_view(["POST"])
# def register(request):
#     serializer = RegisterSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(
#             serializer.data,
#             status=status.HTTP_201_CREATED
#         )
#     return Response(
#         serializer.errors,
#         status=status.HTTP_400_BAD_REQUEST
#     )

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

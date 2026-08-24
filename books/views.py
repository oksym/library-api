from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET", "POST"])
def books(request):
    if request.method=='GET':
        books=Book.objects.all()
        serializer=BookSerializer(books, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



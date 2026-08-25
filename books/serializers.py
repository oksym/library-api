from rest_framework import serializers
from .models import Book, Category, Author
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields="__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class BookSerializer(serializers.ModelSerializer):
    # author=AuthorSerializer()
    # categories =CategorySerializer(many=True)

    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source="author",
        write_only=True
    )

    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        source="categories",
        write_only=True
    )

    class Meta:
        model=Book
        # fields="__all__"
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "price",
            "author",
            "author_id",
            "categories",
            "category_ids",
        ]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"]
        )
        return user
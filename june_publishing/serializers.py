from rest_framework import serializers
from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['id', 'image_url']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['id', 'level']


class BookSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    level = LevelSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

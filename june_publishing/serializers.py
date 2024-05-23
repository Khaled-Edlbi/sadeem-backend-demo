from rest_framework import serializers
from .models import *


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'image_url']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image_url']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['id', 'level']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'language']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subject']


class SeriesMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesMaterial
        fields = ['id', 'series_material']


class BookImageSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'images', 'pdf_url']


class BookSeriesSerializer(serializers.ModelSerializer):
    banners = BannerSerializer(many=True, read_only=True)

    level = LevelSerializer(read_only=True)
    language = LanguageSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)
    series_materials = SeriesMaterialSerializer(many=True, read_only=True)

    books = BookImageSerializer(many=True, read_only=True)

    class Meta:
        model = BookSeries
        fields = '__all__'


class BookSeriesTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSeries
        fields = ['id', 'title', 'author', 'version', 'date', 'summary']


class BookSerializer(serializers.ModelSerializer):
    series = BookSeriesTitleSerializer(read_only=True)

    images = ImageSerializer(many=True, read_only=True)

    category = CategorySerializer(read_only=True)
    level = LevelSerializer(read_only=True)
    language = LanguageSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

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


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['id', 'ar', 'en']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'language']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'ar', 'en']


class SeriesMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesMaterial
        fields = ['id', 'ar', 'en']


class BookImageSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title_ar', 'title_en', 'images', 'pdf_url']


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
    level = LevelSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = BookSeries
        fields = [
            'id',
            'title_ar',
            'title_en',
            'level',
            'subject',
            'version_ar',
            'version_en',
            'date',
            'summary_ar',
            'summary_en'
        ]


class BookSerializer(serializers.ModelSerializer):
    series = BookSeriesTitleSerializer(read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

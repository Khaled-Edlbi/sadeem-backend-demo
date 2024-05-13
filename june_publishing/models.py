from django.db import models
from django.contrib.postgres.fields import ArrayField


class Level(models.Model):
    level = models.CharField(max_length=10)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.level


class Category(models.Model):
    category = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category


class Book(models.Model):
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    level = models.ForeignKey(Level, related_name='levels', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    version = models.CharField()
    date = models.DateField()
    pages_num = models.IntegerField()
    summary = models.TextField()
    views_num = models.IntegerField()
    downloads_num = models.IntegerField()

    pdf_url = models.URLField(max_length=5000)

    series_materials = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    key_features = ArrayField(models.CharField(max_length=None), blank=True, default=list)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BookImage(models.Model):
    for_book = models.ForeignKey(Book, related_name='images', on_delete=models.CASCADE, null=True)
    image_url = models.URLField(max_length=5000)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.for_book}: image-{self.for_book.id}"

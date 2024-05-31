from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    category = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category


class Level(models.Model):
    level = models.CharField(max_length=10)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.level


class Language(models.Model):
    language = models.CharField(max_length=10)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.language


class Subject(models.Model):
    subject = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class SeriesMaterial(models.Model):
    series_material = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.series_material


class BookSeries(models.Model):
    level = models.ForeignKey(Level, related_name='book_series', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name='book_series', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='book_series', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    version = models.CharField(max_length=10)
    date = models.DateField()
    pages_num = models.IntegerField()
    summary = models.TextField()
    views_num = models.IntegerField()
    downloads_num = models.IntegerField()
    series_materials = models.ManyToManyField(SeriesMaterial, related_name='book_series')
    features = ArrayField(models.CharField(), blank=True, default=list)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    series = models.ForeignKey(BookSeries, related_name='books', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    pdf_url = models.URLField(max_length=5000)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"id: {self.id} | {self.title}"


class Banner(models.Model):
    for_series = models.ForeignKey(BookSeries, related_name='banners', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=5000)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.for_series}: image-{self.for_series.id}"


class Image(models.Model):
    for_book = models.ForeignKey(Book, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=5000)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.for_book}: image-{self.for_book.id}"

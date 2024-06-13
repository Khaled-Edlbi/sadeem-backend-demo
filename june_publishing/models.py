from django.db import models
from django.contrib.postgres.fields import ArrayField


class Level(models.Model):
    ar = models.CharField(max_length=50, null=True)
    en = models.CharField(max_length=50, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.en


class Language(models.Model):
    language = models.CharField(max_length=10)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.language


class Subject(models.Model):
    ar = models.CharField(max_length=50, null=True)
    en = models.CharField(max_length=50, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.en


class SeriesMaterial(models.Model):
    ar = models.CharField(max_length=50, null=True)
    en = models.CharField(max_length=50, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.en


class BookSeries(models.Model):
    level = models.ForeignKey(Level, related_name='book_series', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name='book_series', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='book_series', on_delete=models.CASCADE)

    title_ar = models.CharField(max_length=100, null=True)
    title_en = models.CharField(max_length=100, null=True)

    author_ar = models.CharField(max_length=100, null=True)
    author_en = models.CharField(max_length=100, null=True)

    version_ar = models.CharField(max_length=20, null=True)
    version_en = models.CharField(max_length=20, null=True)

    summary_ar = models.TextField(null=True)
    summary_en = models.TextField(null=True)

    date = models.DateField()
    pages_num = models.IntegerField()
    views_num = models.IntegerField()
    downloads_num = models.IntegerField()

    series_materials = models.ManyToManyField(SeriesMaterial, related_name='book_series')

    features_ar = ArrayField(models.CharField(), blank=True, default=list)
    features_en = ArrayField(models.CharField(), blank=True, default=list)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_en


class Book(models.Model):
    series = models.ForeignKey(BookSeries, related_name='books', on_delete=models.CASCADE)

    title_ar = models.CharField(max_length=100, null=True)
    title_en = models.CharField(max_length=100, null=True)

    pdf_url = models.URLField(max_length=5000)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"id: {self.id} | {self.title_en}"


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

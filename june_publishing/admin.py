from django.contrib import admin
from .models import *


admin.site.register(Level)
admin.site.register(Language)
admin.site.register(Subject)
admin.site.register(SeriesMaterial)

admin.site.register(BookSeries)
admin.site.register(Book)

admin.site.register(Banner)
admin.site.register(Image)

from django.urls import path
from .views import *


urlpatterns = [
    path('book-series/<int:pk>', BookSeriesRetrieveAPIView.as_view(), name='book-series'),

    path('books', BooksListAPIView.as_view(), name='books'),
    path('books/<int:pk>', BookRetrieveAPIView.as_view(), name='book'),
    # path('create-book', BookCreateAndUpdateAPIView.as_view(), name='create-book'),
    # path('update-book/<int:pk>', BookCreateAndUpdateAPIView.as_view(), name='update-book'),
]

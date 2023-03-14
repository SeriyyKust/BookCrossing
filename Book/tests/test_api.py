from rest_framework.test import APITestCase
from django.urls import reverse
from Book.models import Book, StateCategory, Genre
from Book.serializers import BookSerializer
from django.contrib.auth.models import User
from rest_framework import status


class BookApiTestCase(APITestCase):

    def test_get(self):
        owner = User.objects.create_user(username="DariDari", password="ilovedrowevery", email="drowmemyfriend@mail.ru")
        state = StateCategory.objects.create(title="Среднее")
        genre_1 = Genre.objects.create(title="Роман")
        genre_2 = Genre.objects.create(title="Роман-антиутопия")
        book_1 = Book.objects.create(title="Преступление и наказание",
                                     description="Социально-психологический и социально-философский роман Фёдора "
                                                 "Михайловича Достоевского",
                                     author="Ф. М. Достоевский",
                                     owner=owner,
                                     state=state,
                                     genre=genre_1,
                                     cover=None)
        book_2 = Book.objects.create(title="1984",
                                     description="Роман-антиутопия Джорджа Оруэлла, изданный в 1949 году.",
                                     author="Джордж Оруэлл",
                                     owner=owner,
                                     state=state,
                                     genre=genre_2,
                                     cover=None)
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BookSerializer([book_1, book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data['results'])

from django.test import TestCase
from Book.serializers import BookSerializer
from Book.models import Book, StateCategory, Genre
from django.contrib.auth.models import User


class BookSerializerTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.owner = User.objects.create_user(username="DariDari", password="ilovedrowevery", email="drowmemyfriend@mail.ru")
        cls.state = StateCategory.objects.create(title="Среднее")
        cls.genre_1 = Genre.objects.create(title="Роман")
        cls.genre_2 = Genre.objects.create(title="Роман-антиутопия")

    def setUp(self):
        self.book_1 = Book.objects.create(title="Преступление и наказание",
                                          description="Социально-психологический и социально-философский роман Фёдора Михайловича Достоевского",
                                          author="Ф. М. Достоевский",
                                          owner=self.owner,
                                          state=self.state,
                                          genre=self.genre_1,
                                          cover=None)
        self.book_2 = Book.objects.create(title="1984",
                                          description="Роман-антиутопия Джорджа Оруэлла, изданный в 1949 году.",
                                          author="Джордж Оруэлл",
                                          owner=self.owner,
                                          state=self.state,
                                          genre=self.genre_2,
                                          cover=None)

    def test_ok(self):
        data = BookSerializer([self.book_1, self.book_2], many=True).data
        expected_data = [
            {
                'id': self.book_1.id,
                'title': "Преступление и наказание",
                'description': "Социально-психологический и социально-философский роман Фёдора Михайловича Достоевского",
                'author': "Ф. М. Достоевский",
                'owner': self.owner.id,
                'state': self.state.title,
                'genre': self.genre_1.title,
                'cover': None
            },
            {
                'id': self.book_2.id,
                'title': "1984",
                'description': "Роман-антиутопия Джорджа Оруэлла, изданный в 1949 году.",
                'author': "Джордж Оруэлл",
                'owner': self.owner.id,
                'state': self.state.title,
                'genre': self.genre_2.title,
                'cover': None
            },
        ]
        self.assertEqual(expected_data, data)

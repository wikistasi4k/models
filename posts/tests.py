from django.test import TestCase
from .models import Author, Post

class AuthorTestCase(TestCase):
    def setUp(self):
        self.author1 = Author.objects.create(nick='JohnDoe', email='johndoe@example.com', bio='Lorem ipsum dolor sit amet.')
        self.author2 = Author.objects.create(nick='JaneDoe', email='janedoe@example.com', bio='Consectetur adipiscing elit.')

    def test_author_count(self):
        self.assertEqual(Author.objects.count(), 2)

    def test_author_str(self):
        self.assertEqual(str(self.author1), 'JohnDoe')

class PostTestCase(TestCase):
    def setUp(self):
        self.author1 = Author.objects.create(nick='JohnDoe', email='johndoe@example.com', bio='Lorem ipsum dolor sit amet.')
        self.post1 = Post.objects.create(title='First Post', content='This is my first post.', author=self.author1)

    def test_post_count(self):
        self.assertEqual(Post.objects.count(), 1)

    def test_post_str(self):
        self.assertEqual(str(self.post1), 'First Post')


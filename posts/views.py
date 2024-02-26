from django.shortcuts import render
from .models import Author, Post

def create_sample_instances(request):
    # Utwórz autorów
    author1 = Author.objects.create(nick='JohnDoe', email='johndoe@example.com', bio='Lorem ipsum dolor sit amet.')
    author2 = Author.objects.create(nick='JaneDoe', email='janedoe@example.com', bio='Consectetur adipiscing elit.')

    # Utwórz posty
    post1 = Post.objects.create(title='First Post', content='This is my first post.', author=author1)
    post2 = Post.objects.create(title='Second Post', content='This is my second post.', author=author2)

    return render(request, 'create_sample_instances.html')
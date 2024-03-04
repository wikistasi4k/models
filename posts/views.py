from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Post
from .forms import AuthorForm, PostForm

def create_sample_instances(request):
    return render(request, 'create_sample_instances.html')

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})

def author_details(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author_details.html', {'author': author})

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts_list.html', {'posts': posts})

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_details.html', {'post': post})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors_list')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})
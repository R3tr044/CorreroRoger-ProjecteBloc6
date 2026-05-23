from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag

def starting_page(request):
    # Usamos el ORM en vez de una lista FAKE
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, "blog/all-posts.html", {
        "posts": all_posts 
    })

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })

def authors_list(request):
    all_authors = Author.objects.all()
    return render(request, "blog/authors-list.html", {
        "authors": all_authors
    })

def author_detail(request, author_id):
    # Esto busca al autor en la BBDD. Si no existe, da error 404.
    author = get_object_or_404(Author, id=author_id)
    # Esto filtra los posts asociados a ese autor.
    posts = Post.objects.filter(author=author).order_by('-date')
    
    return render(request, "blog/author_detail.html", {
        "author": author,
        "posts": posts
    })

def tags_list(request):
    all_tags = Tag.objects.all() 
    return render(request, "blog/tags.html", {
        "tags": all_tags  
    })

def tag_posts(request, tag_name):
    tag = get_object_or_404(Tag, tag=tag_name) 
    posts_with_tag = Post.objects.filter(tags=tag).order_by('-date')
    return render(request, "blog/tag-posts.html", {
        "tag": tag,
        "posts": posts_with_tag
    })
from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name="starting-page"),
    path('posts', views.posts, name="posts-page"),
    path('posts/<slug:slug>', views.post_detail, name="post-detail-page"),
    
    # Lista de autores
    path('authors', views.authors_list, name="authors-page"),
    
    # Detalle de autor (usaremos el ID, que es lo más limpio)
    path('authors/<int:author_id>/', views.author_detail, name="author-detail"),
    
    path('tags', views.tags_list, name="tags-page"),
    path('tags/<str:tag_name>', views.tag_posts, name='tag-posts'),
]
from django.db import models
class Author(models.Model):
    """
    Model que representa l'autor d'un post del blog.
    Conté informació bàsica com el nom, cognoms i correu electrònic.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Tag(models.Model):
    """
    Model que representa una etiqueta o categoria per als posts.
    Permet classificar i filtrar les entrades del blog.
    """
    tag = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.tag
class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=250)
    # CAMBIO AQUÍ: Usamos ImageField en lugar de CharField
    image = models.ImageField(upload_to="posts", null=True) 
    date = models.DateField()
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts")
    
    def __str__(self):
        return self.title
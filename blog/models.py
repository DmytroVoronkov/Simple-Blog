from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=254)


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    content = models.TextField(validators=[MinLengthValidator(20)])

    author = models.ForeignKey(
        "author", on_delete=models.SET_NULL, related_name="posts"
    )

    def __str__(self) -> str:
        return self.slug

from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    content = models.TextField(validators=[MinLengthValidator(20)])

    def __str__(self) -> str:
        return self.slug
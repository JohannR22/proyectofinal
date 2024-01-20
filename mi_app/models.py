from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=100, default='Autor desconocido')
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
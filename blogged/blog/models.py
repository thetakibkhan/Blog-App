from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class meta:
        ordering = ('-created_at')
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class meta:
        ordering = ('-created_at')
    def __str__(self):
        return f'{self.name} - {self.content[:50]}...'

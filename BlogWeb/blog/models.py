from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_post', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_post', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})

    def total_likes(self):
        return self.likes.count()
    def total_dislikes(self):
        return self.dislikes.count()
class Comment(models.Model):
    post=models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(Auto_now_add=True)
    
# comment part
    def __str__ (self):
        return '%s - %s' % (self.post.title, self.name)
    


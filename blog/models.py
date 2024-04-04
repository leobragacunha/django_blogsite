from django.db import models
from django.urls import reverse

from accounts.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField("Created on", auto_now_add=True)
    updated_date = models.DateTimeField("Updated on", auto_now=True)
    blogger = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    created_date = models.DateTimeField("Created on", auto_now_add=True)
    updated_date = models.DateTimeField("Updated on", auto_now=True)
    comment_blogger = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name='comments')
    comment = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.comment_blogger} on {self.post} at {self.updated_date}"

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.post.pk})
    


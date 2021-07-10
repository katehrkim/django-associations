from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"USER: {self.name}"

# one to many
class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField
    user = models.ForeignKey(User, related_name="post", on_delete=models.CASCADE)

    def __str__(self):
        return f"POST: {self.title}"

# one to many w/ user and post
class Comment(models.Model):
    content = models.TextField
    user = models.ForeignKey(User, related_name="comment", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)

    def __str__(self):
        return f"COMMENT: {self.user} said {self.content} on {self.post}"


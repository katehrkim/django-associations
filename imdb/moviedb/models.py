from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Actor(models.Model):
    actor_name = models.CharField(max_length=64)

    def __str__(self):
        return f"ACTOR: {self.actor_name}"

# many to many
class Movie(models.Model):
    movie_name = models.CharField(max_length=64)
    actors = models.ManyToManyField(Actor, through="Role", related_name="movies")

    def __str__(self):
        return f"MOVIE: {self.movie_name}"

# many to many, join table
class Role(models.Model):
    actor = models.ForeignKey(Actor, on_delete=CASCADE, related_name="roles")
    movie = models.ForeignKey(Movie, on_delete=CASCADE, related_name="roles")

    def __str__(self):
        return f"ROLE: {self.actor} plays in {self.movie}"

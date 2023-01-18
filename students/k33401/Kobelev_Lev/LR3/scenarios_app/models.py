from django.db import models
from django.contrib.auth import get_user_model
import datetime


User = get_user_model()


class GameSystem(models.Model):
    name = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return self.name


class Scenario(models.Model):
    name = models.CharField(max_length=31)
    short_description = models.CharField(max_length=255)
    full_description = models.TextField()
    game_system = models.ForeignKey(GameSystem, on_delete=models.SET_NULL, null=True)
    is_completed = models.BooleanField()
    is_age_restricted = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    publish_date = models.DateField(default=datetime.date.today)
    image = models.TextField(default='https://raw.githubusercontent.com/evlko/ITMO-ICT-Frontend-2022/main/labs/K33401/Kobelev/LR1/img/image-1.png')

    def __str__(self):
        return self.name


class Review(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='scenario')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    text = models.TextField()
    publish_date = models.DateField(default=datetime.date.today)
    is_edited = models.BooleanField(default=False)

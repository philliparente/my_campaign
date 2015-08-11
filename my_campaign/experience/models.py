from django.db import models

class Character(models.Model):
    character_name = models.CharField(max_length=200)

class Session(models.Model):
    session_title = models.CharField(max_length=200)
    session_date = models.DateTimeField()
    session_characters = models.ForeignKey(Character)

# Create your models here.

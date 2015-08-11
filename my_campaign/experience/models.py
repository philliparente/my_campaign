from django.db import models

class Character(models.Model):
    character_name = models.CharField(max_length=200)

    def __str__(self):
        return self.character_name


class Session(models.Model):
    session_title = models.CharField(max_length=200)
    session_date = models.DateTimeField()
    session_characters = models.ForeignKey(Character)

    def __str__(self):
	return self.session_title

# Create your models here.

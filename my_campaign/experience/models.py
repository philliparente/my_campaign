from django.db import models


class Campaign(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()


class Session(models.Model):
    title = models.CharField(max_length=200, blank=False)
    date = models.DateTimeField()

    def __str__(self):
	return self.title


class Character(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.CharField(max_length=200, blank=False)
    campaign = models.ForeignKey(Campaign)
    characters = models.ManyToManyField(Session, related_name='participating')

    def __str__(self):
        return self.name
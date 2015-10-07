from django.db import models


class Campaign(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.title


class Session(models.Model):
    title = models.CharField(max_length=200, blank=False)
    date = models.DateTimeField()
    characters = models.ManyToManyField('Character', related_name='participating')

    def __str__(self):
        return self.title


class Criteria(models.Model):
    title = models.CharField(max_length=200, blank=False)
    value = models.DecimalField(max_digits=4, decimal_places=0, blank=False)

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.CharField(max_length=200, blank=False)
    campaign = models.ForeignKey(Campaign)
    characters = models.ManyToManyField('Session', related_name='participating')

    def __str__(self):
        return self.name
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    edition = models.PositiveIntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.title

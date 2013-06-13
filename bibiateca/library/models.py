from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, null=True, blank=True)
    edition = models.PositiveIntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.title


class Series(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class Comics(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    series = models.ForeignKey(Series, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, null=True, blank=True)

    def __unicode__(self):
        return self.title

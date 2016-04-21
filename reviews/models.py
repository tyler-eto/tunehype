from __future__ import unicode_literals

from django.db import models
import numpy as np


class Song(models.Model):
    name = models.CharField(max_length=200)

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __unicode__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    # RATING_CHOICES = (
    #     ('barf', 'barf'),
    #     ('meh', 'meh'),
    #     ('aight', 'aight'),
    #     ('sick', 'sick'),
    #     ('hype-worthy', 'hype-worthy')
    # )
    song = models.ForeignKey(Song)
    pub_date = models.DateTimeField('date_published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
    # rating = models.CharField(choices=RATING_CHOICES)
    tags = models.CharField(max_length=200)

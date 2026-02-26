# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class User(models.Model):

    #__User_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Publisher(models.Model):

    #__Publisher_FIELDS__
    popularity_score = models.IntegerField(null=True, blank=True)

    #__Publisher_FIELDS__END

    class Meta:
        verbose_name        = _("Publisher")
        verbose_name_plural = _("Publisher")


class Author(models.Model):

    #__Author_FIELDS__
    address = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=255, null=True, blank=True)
    joindate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    popularity_score = models.IntegerField(null=True, blank=True)
    followers = models.ForeignKey(User, on_delete=models.CASCADE)

    #__Author_FIELDS__END

    class Meta:
        verbose_name        = _("Author")
        verbose_name_plural = _("Author")


class Book(models.Model):

    #__Book_FIELDS__
    genre = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    author = models.CharField(max_length=255, null=True, blank=True)
    publisher = models.CharField(max_length=255, null=True, blank=True)

    #__Book_FIELDS__END

    class Meta:
        verbose_name        = _("Book")
        verbose_name_plural = _("Book")



#__MODELS__END

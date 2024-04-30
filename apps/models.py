from django.db import models


class Person(models.Model):
    fullname = models.CharField(max_length=223)
    username = models.CharField(max_length=100)
    user_id = models.IntegerField()

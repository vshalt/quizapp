from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=250, unique=True, null=False)
    capital = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.name


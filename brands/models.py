from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name

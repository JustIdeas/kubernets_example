from django.db import models

class store(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    def __str__(self) -> str:
        return self.name


from django.db import models

# Create your models here.
class Grocery(models.Model):
    name = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name[0:50]

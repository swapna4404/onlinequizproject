from django.db import models
from django.contrib.auth.models import User

class Typeform(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_by = models.TextField(max_length=100)
    

    def _str_(self):
        return self.title

# Create your models here.

from django.db import models
from django.contrib.auth.models import User # Import models to connect

STATUS = ((0, "New-request"), (1, "Pre-requested"))

# Create your models here.
class Post(models.Model):
    type = models.CharField(max_length=200, unique=True)
    start = models.DateField()
    end = models.DateField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
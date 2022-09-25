from asyncio.windows_events import NULL
from datetime import datetime
import email
from pickle import TRUE
from pyexpat import model
from re import T
from venv import create
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
# Create your models here.


class Cashbook(models.Model):
    title = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('data published')
    content = models.TextField()
    email = models.EmailField(max_length=254, blank=True)
    url = models.URLField(max_length=200, blank= True)
    created_at = models.DateTimeField(default= datetime.now, blank=True)

    def __str__(self):
        return self.title
#####################################################




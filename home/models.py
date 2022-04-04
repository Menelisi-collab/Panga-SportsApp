from django.db import models


class Entities(models.Model):
    name = models.CharField(max_length=80)
    image_url = models.CharField(max_length=2083)











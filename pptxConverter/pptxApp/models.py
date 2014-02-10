from django.db import models


class Presentation(models.Model):
    title = models.CharField(max_length=50)
    presentation = models.CharField(max_length=500)


class PresentationImages(models.Model):
    presentation = models.ForeignKey(Presentation)
    image = models.CharField(max_length=500)
    image_min = models.CharField(max_length=500)
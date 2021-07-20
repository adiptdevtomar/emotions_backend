from django.db import models


class EmotionModel(models.Model):
    text = models.CharField(blank=False, max_length=3000)

# models.py
from django.db import models

class KanjiWord(models.Model):
    kanji = models.CharField(max_length=10)
    reading = models.CharField(max_length=20)

    def __str__(self):
        return self.kanji
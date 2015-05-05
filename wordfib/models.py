from django.db import models

# Create your models here.
class WordAndTrue(models.Model):
    word = models.CharField(max_length=50)
    real_definition = models.CharField(max_length=700)

class FakeDefinitions(models.Model):
    real_word = models.ForeignKey(WordAndTrue)
    fake_definition = models.CharField(max_length=700)
    votes = models.IntegerField(default=0)
    author = models.CharField(max_length=20)
    

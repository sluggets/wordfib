from django.db import models

# Create your models here.
class WordAndTrue(models.Model):
    word = models.CharField(max_length=50)
    real_definition = models.CharField(max_length=700, blank=True, null=True)
    definition = models.CharField(max_length=700)
    def __str__(self):
        return self.word

class FakeDefinitions(models.Model):
    real_word = models.ForeignKey(WordAndTrue)
    fake_definition = models.CharField(max_length=700, blank=True, null=True)
    definition = models.CharField(max_length=700)
    votes = models.IntegerField(default=0)
    author = models.CharField(max_length=20)
    def __str__(self):
        return self.author

    def score(self):
        return self.votes
    
    def fake_def(self):
        return self.fake_definition 

class CorrectGuess(models.Model):
    user = models.CharField(max_length=20, unique=True)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.user

    def score_from_correct(self):
        return self.score

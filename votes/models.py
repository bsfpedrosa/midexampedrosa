from django.db import models

# Create your models here.
class Candidate(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    position = models.ForeignKey(Position,on_delete=models.CASCADE,related_name="positions")
    birthdate = models.DateTimeField('birthday')
    platform = models.TextField()

    def __str__(self):
        return 'Candidates: {}'.format(self.lastname)

class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE,related_name="candidates")
    vote_datetime = models.DateTimeField('vote date-time')

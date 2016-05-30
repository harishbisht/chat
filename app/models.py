from django.db import models
from datetime import datetime

class NewPerson(models.Model):
    session_id = models.CharField(max_length=20, blank=True)
    time = models.DateTimeField(default=datetime.now)  #1 for active  0 for inactive
    connected = models.BooleanField(default=False)
      
    def __str__(self):
        return self.session_id


class Waiting(models.Model):
    session_id = models.OneToOneField(NewPerson)


class Pairing(models.Model):
    user1 = models.ForeignKey(NewPerson,related_name = "first")
    user2 = models.ForeignKey(NewPerson,related_name = "second")


class Message(models.Model):
    session_id = models.ForeignKey(NewPerson)
    message = models.CharField(max_length=400, blank=True)


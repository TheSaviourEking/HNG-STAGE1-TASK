from django.db import models

class GetApi(models.Model):
    slackUsername = models.CharField(max_length=200)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.CharField(max_length=200)


    def __str__(self):
        return self.slackUsername
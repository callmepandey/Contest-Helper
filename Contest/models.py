from django.db import models

class MyContest(models.Model):
    contestName = models.CharField(max_length = 50)
    def __str__(self):
        return self.contestName


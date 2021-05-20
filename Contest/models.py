from django.db import models
class Platforms(models.TextChoices):
    Codeforces = 'Codeforces' , 'Codeforces'
    Codechef = 'Codechef' , 'Codechef'
    Atcoder = 'AtCoder' , 'Atcoder'
class MyContest(models.Model):
    contestName = models.CharField(max_length = 50 )
    dateTime = models.DateTimeField()
    platform = models.CharField(max_length = 20, choices = Platforms.choices , default = Platforms.Codeforces)
    contestLink = models.URLField(max_length = 200)
    def __str__(self):
        return self.contestName


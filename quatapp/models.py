from django.db import models

class Profits(models.Model):
    date = models.DateField(blank=True, null=True)
    usd = models.IntegerField(blank=True, null=True)
    inr = models.IntegerField(blank=True, null=True)
    result = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.result

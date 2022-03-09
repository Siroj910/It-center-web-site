from django.db import models


class Drop(models.Model):
    DataName = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.DataName


class SaveDrop(models.Model):
    UserName = models.CharField(max_length=100)
    UserNumber = models.IntegerField()
    DataSave = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.UserName},{self.UserNumber},{self.DataSave}"

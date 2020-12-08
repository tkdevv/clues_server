from django.db import models

class LatestVersion(models.Model):
    version = models.IntegerField(unique=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "version " + str(self.version)


class Card(models.Model):
    clues = models.CharField(max_length=255)

    def __str__(self):
        return "card " + str(self.id)

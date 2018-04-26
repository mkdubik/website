from django.db import models

class Visitor(models.Model):
    ip = models.CharField(max_length=45, blank=False, null=False)
    ua = models.CharField(max_length=100, blank=True, null=False)
    referer = models.URLField()
    path = models.URLField()

    class Meta:
        unique_together = (('ip', 'path'),)

    def __str__(self):
       return self.ip
from django.db import models
from ckeditor.fields import RichTextField


class Log(models.Model):
    brew_type = models.CharField(max_length=50, blank=False, null=False)
    yeast = models.CharField(max_length=50, blank=False, null=False)
    yeast_addition = models.DateTimeField(blank=False, null=False)
    fruit = models.DecimalField(max_digits=5, decimal_places=3)
    sugar = models.DecimalField(max_digits=5, decimal_places=3)
    juice = models.DecimalField(max_digits=5, decimal_places=3)
    water = models.DecimalField(max_digits=5, decimal_places=3)
    preprocess = RichTextField(extra_plugins=['image2'])
    process = RichTextField(extra_plugins=['image2'])
    og = models.DecimalField(max_digits=4, decimal_places=3)
    fg = models.DecimalField(max_digits=4, decimal_places=3)
    extra = RichTextField(extra_plugins=['image2'])

    def __str__(self):
        return ''.join([self.brew_type,' - ', self.yeast_addition.strftime("%A, %d. %B %Y %I:%M%p")])

class LogEntry(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    temperature = models.CharField(max_length=10, blank=False, null=False)
    sg = models.DecimalField(max_digits=4, decimal_places=3, null=False)
    extra = RichTextField(extra_plugins=['image2'])

    def __str__(self):
        return 'Entry ' + self.date.strftime("%A, %d. %B %Y %I:%M%p") + ' at ' + ''.join([self.log.brew_type,' - ', self.log.yeast_addition.strftime("%A, %d. %B %Y %I:%M%p")])

from django.db import models
from ckeditor.fields import RichTextField

class Temperature(models.Model):
    timestamp = models.IntegerField(blank=False, null=False)
    temperature = models.IntegerField(blank=False, null=False)
    location = models.CharField(max_length=50, blank=False, null=False)

class Log(models.Model):
    brew_type = models.CharField(max_length=50, blank=False, null=False)
    slug = models.SlugField()
    yeast = models.CharField(max_length=50, blank=False, null=False)
    yeast_addition = models.DateTimeField(blank=False, null=False)
    fruit = models.DecimalField(max_digits=5, decimal_places=3)
    sugar = models.DecimalField(max_digits=5, decimal_places=3)
    juice = models.DecimalField(max_digits=5, decimal_places=3)
    water = models.DecimalField(max_digits=5, decimal_places=3)
    process = RichTextField(extra_plugins=['image2'])
    og = models.DecimalField(max_digits=4, decimal_places=3)
    fg = models.DecimalField(max_digits=4, decimal_places=3)
    label = models.ImageField(blank=True, null=True)

    def __str__(self):
        return ''.join([self.brew_type,' - ', self.yeast_addition.strftime("%A, %d. %B %Y %I:%M%p")])

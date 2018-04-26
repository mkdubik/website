from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    slug = models.SlugField(unique=True, editable=False)
    title = models.CharField(max_length=200, blank=False, null=False)
    content = RichTextField(extra_plugins=['image2'])
    like = models.IntegerField(null=False, default=0, editable=False)
    published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
       return '%s - %s' % (self.title, self.created.strftime('%a %d %b %Y, %H:%M'))

from django.db import models
from django.conf import settings
import os
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    image = models.ImageField()
    tags = models.ManyToManyField(Tag, related_name='photos')


    def image_tag(self):
        from django.utils.html import mark_safe
        # image_path = '/' + str(self.image)
        return mark_safe('<img src="/%s" width=250px/>' % str(self.image))
    image_tag.short_description = 'Image'
    # image_tag.allow_tags = True


    def __str__(self):
        return self.name

    # def import_photos(self, path):
    #     load_images(path)
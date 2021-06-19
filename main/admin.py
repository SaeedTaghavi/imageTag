from django.contrib import admin
from main.models import Photo, Tag
from main.scripts import load_images
# Register your models here.


@admin.action(description='load images')
def make_published(modeladmin, request, queryset):
    load_images('/home/sarah/Pictures')

class PhotoAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'image_tag', 'tags' )
    readonly_fields = ('image_tag',)
    list_display = ['name', 'image']
    actions = [make_published]



admin.site.register(Photo, PhotoAdmin)
admin.site.register(Tag)

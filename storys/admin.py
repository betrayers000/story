from django.contrib import admin
from .models import Story, StoryImage, Comment

# Register your models here.
admin.site.register(Story)
admin.site.register(StoryImage)
admin.site.register(Comment)
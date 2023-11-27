from django.contrib import admin
from . import models

admin.site.register(models.Room)
admin.site.register(models.SubRoom)
admin.site.register(models.Puzzle)
admin.site.register(models.Solution)
admin.site.register(models.Reward)
admin.site.register(models.Hint)
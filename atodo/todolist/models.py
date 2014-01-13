from django.db import models
from django.contrib import admin

import datetime

class List(models.Model):
    title = models.CharField(max_length=250, unique=True)

    def __unicode__(self):
        return self.title

    
    

    

class Item(models.Model):
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "priority", "difficulty", "created", "done"]
    search_fields = ["name"]

admin.site.register(Item, ItemAdmin)
admin.site.register(List)

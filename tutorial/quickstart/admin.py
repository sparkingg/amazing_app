from django.contrib import admin

# Register your models here.

from tutorial.quickstart.models import Dag, Tweet, Follow

admin.site.register(Dag)
admin.site.register(Tweet)
admin.site.register(Follow)

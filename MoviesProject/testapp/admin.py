from django.contrib import admin
from testapp.models import input_movie
# Register your models here.

class inputmovieAdmin(admin.ModelAdmin):
    list_display = ['name','rating']

admin.site.register(input_movie, inputmovieAdmin)
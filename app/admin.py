from django.contrib import admin
from .models import ToDo_Model

class ToDO_Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'details', 'Date')

admin.site.register(ToDo_Model, ToDO_Admin)


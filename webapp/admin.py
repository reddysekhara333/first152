from django.contrib import admin

# Register your models here.
from webapp.models import modelform
class adminmod(admin.ModelAdmin):
    list_display = ['name','company','salary']
admin.site.register(modelform,adminmod)
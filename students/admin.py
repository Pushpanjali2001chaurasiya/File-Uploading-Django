from django.contrib import admin
from .models import registration 

admin.site.register(registration)
admin.site.site_header='ADIT_REGISTRAION PORTAL'
admin.site.site_title='students registration'
admin.site.index_title='ADIT_NSTI'


class registration(admin.ModelAdmin):
    list_display=('id','name','docu')

# Register your models here.

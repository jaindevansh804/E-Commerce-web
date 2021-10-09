from django.contrib import admin
from Website import models

# Register your models here.
class WebsiteAdmin(admin.ModelAdmin):
    class Media:            
        js = ("js/main.js",)

admin.site.register(models.Products, WebsiteAdmin)
admin.site.register(models.Contact)
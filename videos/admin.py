from django.contrib import admin
from . import models
# Register your models here.

class MovieAdmin(admin.ModelAdmin):# stick to this naming convention

    fields = ['release_year','title','length'] #fields detail view render ordering in admin is done in the fields list in class named like this ClasAdmin
    
    search_fields=['title','length']# list of search terms to be rendered 
    
    list_filter=['release_year','length','title'] #for filters
    
    list_display=['pk','release_year','length','title']# list display ---order sensitive
    
    
    list_editable=['length']# make field editable
    
    


admin.site.register(models.Customer)

admin.site.register(models.Movie,MovieAdmin)






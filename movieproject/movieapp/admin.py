from django.contrib import admin

# Register your models here.
from . models import Category,Movies
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category,CategoryAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 20
admin.site.register(Movies,MovieAdmin)
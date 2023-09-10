from django.contrib import admin

# Register your models here.
from .models import Street, City, Magazine


class StreetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Street, StreetAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(City, CityAdmin)


class MagazineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'street', 'house', 'time_open', 'time_close')
    list_display_links = ('id', 'name')



admin.site.register(Magazine, MagazineAdmin)
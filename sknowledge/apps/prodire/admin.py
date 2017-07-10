from django.contrib import admin
from prodire.models import Pro_icon
# Register your models here.

# class Pro_iconAdmin(admin.ModelAdmin):

#     fields = ('icon_name', 'photo_tag', )
#     readonly_fields = ('photo_tag',)
# admin.site.register(Pro_icon, Pro_iconAdmin)
admin.site.register(Pro_icon)

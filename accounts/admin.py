from django.contrib import admin

from . import models

from blog import models as blog_models

# Register your models here.

class PostInline(admin.StackedInline):
    model= blog_models.Post
    extra = 0


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'date_of_birth')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'first_name', 'last_name', 'password')}),
        ("Adittional Info", {'fields': ('date_of_birth','bio')}),
        )
    
    inlines = [PostInline]

admin.site.register(models.User, UserAdmin)
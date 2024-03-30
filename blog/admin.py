from django.contrib import admin

from . import models

# Register your models here.

class CommentInline(admin.StackedInline):
    model = models.Comment
    extra = 0


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('created_date','title', 'blogger')
    list_filter = ('created_date', 'blogger')
    ordering = ('-created_date',)

    inlines=[CommentInline]
    


admin.site.register(models.Comment)
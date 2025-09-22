from django.contrib import admin
from comments.models import Comment

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'post', 'created_at')
    search_fields = ('content', 'user__username', 'post__title')
    list_filter = ('created_at', 'updated_at', 'user', 'post')
    ordering = ('-created_at',)
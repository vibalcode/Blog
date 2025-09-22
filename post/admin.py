from django.contrib import admin
from post.models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_at', 'user', 'category')
    list_filter = ('published', 'created_at', 'updated_at', 'user', 'category')
    search_fields = ('title', 'content', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)
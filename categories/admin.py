from django.contrib import admin
from .models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('title', 'published') # muestra estos campos en la lista de categorias
  prepopulated_fields = {'slug': ('title',)} # sirve para autocompletar el slug
  list_filter = ('published',) # filtro por publicado o no
  search_fields = ('title', 'slug') # campo de busqueda por titulo y slug
from django.contrib import admin
from recipes.models import Recipe, Ingredient, SavedRecipe

# Register your models here.

admin.site.register(SavedRecipe)

class IngredientInlineAdmin(admin.TabularInline):
    model = Ingredient

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'method')
    inlines = (IngredientInlineAdmin, )

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'recipe')

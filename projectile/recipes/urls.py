from django.urls import path, include
from recipes.views import RecipeList, RecipeDetail, CreateRecipe, SaveRecipe, SavedRecipeList, SavedRecipeDetail, IngredientDetail


urlpatterns = [
    path(
        'recipe_list/', RecipeList.as_view(), name='recipe_list'
    ),
    path(
        'add_recipe/', CreateRecipe.as_view(), name="create_recipe"
    ),
     path(
         '<int:pk>/', RecipeDetail.as_view(), name='recipe_detail'
    ),
    path(
        'ingredient/<int:pk>/', IngredientDetail.as_view(), name='ingredient_detail'
    ),
    path(
        'save_recipe/', SaveRecipe.as_view(), name='save_recipe'
        ),
    path(
        'saved_recipe_list/', SavedRecipeList.as_view(), name='saved_recipe_list'
    ),
    path(
        'saved_recipe/<int:pk>/', SavedRecipeDetail.as_view(), name='saved_recipe_detail'
    ),
]
from .models import Recipe, Ingredient, SavedRecipe
import json
from django.contrib.auth.models import User
from user.serializers import UserSerializer
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'item', 'quantity']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(source='ingredient_set', many=True)
    author = UserSerializer(read_only=True)
    image = Base64ImageField()
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'author', 'pub_date', 'ingredients', 'method', 'image']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredient_set')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient)
        return recipe

class SavedRecipeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    recipe = RecipeSerializer(read_only=True)
    class Meta:
        model = SavedRecipe
        fields = ['id', 'recipe', 'user']


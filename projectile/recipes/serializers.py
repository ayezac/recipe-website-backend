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

    def update(self, instance, validated_data):
        if validated_data.get('image') != None:
            instance.image = validated_data.get('image', instance.image)
       
        instance.title = validated_data.get('title', instance.title)
        instance.method = validated_data.get('method', instance.method)
        ingredients_data = validated_data.pop('ingredient_set')
        instance.save()
        ingredients =[]
        ingredients_ids = [ingredient.id for ingredient in instance.ingredient_set.all()]

        for ingredient_data in ingredients_data:
            if 'id' in ingredient_data.keys():
                if Ingredient.objects.filter(id=ingredient_data['id']).exists():
                    ingredient = Ingredient.objects.get(id=ingredient_data['id'])
                    ingredient.item = ingredient_data.get('item', ingredient.item)
                    ingredient.quantity = ingredient_data.get('quantity', ingredient.quantity)
                    ingredient.save()
                    ingredients.append(ingredient.id)
                else:
                    continue
            else:
                ingredient = Ingredient.objects.create(**ingredient_data, recipe=instance)
                ingredients.append(ingredient.id)
        
        for ingredient in instance.ingredient_set.all():
            if ingredient.id not in ingredients:
                ingredient.delete()
    
        return instance

class SavedRecipeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    recipe = RecipeSerializer(read_only=True)
    class Meta:
        model = SavedRecipe
        fields = ['id', 'recipe', 'user']


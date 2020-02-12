from .models import Recipe, SavedRecipe, Ingredient
from django.contrib.auth.models import User
from .serializers import RecipeSerializer, SavedRecipeSerializer, IngredientSerializer
from rest_framework.views import APIView
from rest_framework import generics, views, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import filters

# Create your views here.
class RecipeGeneric:
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeList(RecipeGeneric, generics.ListAPIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'ingredient__item']

@permission_classes((IsAuthenticated,))
class CreateRecipe(APIView):
    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
       
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class RecipeDetail(RecipeGeneric, generics.RetrieveUpdateDestroyAPIView):
#     pass
class RecipeDetail(APIView):
    def get_object(self, pk):
        try:
            print(Recipe.objects.get(pk=pk).image)
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        recipe = self.get_object(pk=pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        recipe = self.get_object(pk=pk)
        serializer = RecipeSerializer(recipe, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        recipe = self.get_object(pk=pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

@permission_classes((IsAuthenticated,))
class SaveRecipe(APIView):
    def post(self, request, format=None):
        serializer = SavedRecipeSerializer(data=request.data)
        recipe_id = request.data.get('recipe')
        recipe = Recipe.objects.get(id=recipe_id)
     
        if serializer.is_valid():  
            try:
                serializer.save(user=request.user, recipe=recipe)
                serializer.is_valid(raise_exception=True)
            except Exception as msg:
                if str(msg) == "UNIQUE constraint failed: recipes_savedrecipe.recipe_id, recipes_savedrecipe.user_id":
                    return JsonResponse({'message': str(msg)})       
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SavedRecipeList(generics.ListAPIView):
    queryset = SavedRecipe.objects.all()
    serializer_class = SavedRecipeSerializer

class SavedRecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SavedRecipe.objects.all()
    serializer_class = SavedRecipeSerializer

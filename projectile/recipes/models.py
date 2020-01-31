from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    method = models.TextField(max_length=None)
    image = models.ImageField(upload_to="recipe_images", null=True, blank=True)

    def __str__(self):
        return self.title
        

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True, blank=True)
    item = models.CharField(max_length=300)
    quantity = models.CharField(max_length=300)

    def __str__(self):
        return self.item 

class SavedRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ('recipe', 'user',)
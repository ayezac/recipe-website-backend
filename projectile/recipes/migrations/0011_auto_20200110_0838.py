# Generated by Django 2.2.7 on 2020-01-10 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_savedrecipe_is_saved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe'),
        ),
        migrations.DeleteModel(
            name='SavedRecipe',
        ),
    ]

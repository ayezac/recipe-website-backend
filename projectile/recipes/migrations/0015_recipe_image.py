# Generated by Django 2.2.7 on 2020-01-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_remove_savedrecipe_is_saved'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipe_images/'),
        ),
    ]

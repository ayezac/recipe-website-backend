# Generated by Django 2.2.7 on 2019-12-09 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20191129_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

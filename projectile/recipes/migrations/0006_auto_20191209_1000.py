# Generated by Django 2.2.7 on 2019-12-09 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20191209_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.CharField(blank='True', max_length=200, null=True),
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-06 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articulo',
            new_name='Article',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
    ]

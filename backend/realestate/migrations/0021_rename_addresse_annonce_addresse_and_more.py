# Generated by Django 4.1.4 on 2023-01-31 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0020_alter_photo_annonce'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annonce',
            old_name='addresse',
            new_name='Addresse',
        ),
        migrations.RenameField(
            model_name='annonce',
            old_name='categorie',
            new_name='Categorie',
        ),
        migrations.RenameField(
            model_name='annonce',
            old_name='commune',
            new_name='Commune',
        ),
        migrations.RenameField(
            model_name='annonce',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='annonce',
            old_name='prix',
            new_name='Prix',
        ),
        migrations.RenameField(
            model_name='annonce',
            old_name='surface',
            new_name='Surface',
        ),
        migrations.RenameField(
            model_name='annonce',
            old_name='type',
            new_name='Type',
        ),
        migrations.RenameField(
            model_name='annonce',
            old_name='wilaya',
            new_name='Wilaya',
        ),
        migrations.AddField(
            model_name='annonce',
            name='titre',
            field=models.CharField(default='nouvelle annonce', max_length=25),
        ),
    ]
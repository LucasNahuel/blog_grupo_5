# Generated by Django 4.2.7 on 2023-12-16 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_creador_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_post'),
        ),
    ]
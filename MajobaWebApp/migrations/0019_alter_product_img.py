# Generated by Django 4.2.3 on 2023-08-01 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MajobaWebApp', '0018_task_taker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(default='media/cal.jfif', null=True, upload_to='media/productos/', verbose_name='Imagen'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-20 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MajobaWebApp', '0005_alter_employee_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='img',
            field=models.ImageField(null=True, upload_to='media/empleados/'),
        ),
    ]
# Generated by Django 4.1.7 on 2023-07-19 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MajobaWebApp', '0016_category_type_employee_type_machine_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.IntegerField(default=4),
        ),
    ]

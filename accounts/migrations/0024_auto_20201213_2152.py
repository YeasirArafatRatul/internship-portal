# Generated by Django 3.0.7 on 2020-12-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20201127_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='passing_year',
            field=models.DateField(),
        ),
    ]

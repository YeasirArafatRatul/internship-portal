# Generated by Django 3.0.7 on 2020-11-27 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_benefits_course_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='employee_no',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]

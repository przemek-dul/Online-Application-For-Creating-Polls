# Generated by Django 4.0.3 on 2022-04-10 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_questionnaire_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='multiple_choice',
            field=models.BooleanField(default=False),
        ),
    ]

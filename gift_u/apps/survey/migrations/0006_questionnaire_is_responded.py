# Generated by Django 3.0.2 on 2020-02-25 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_choiceanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='is_responded',
            field=models.BooleanField(blank=True, default=False, verbose_name='是否收到回覆'),
        ),
    ]
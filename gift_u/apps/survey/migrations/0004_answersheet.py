# Generated by Django 3.0.2 on 2020-02-19 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0003_auto_20200130_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('extra_messages', models.CharField(blank=True, default='', max_length=200, verbose_name='回覆一些文字給他吧')),
                ('done', models.BooleanField(default=False, help_text='乙完成回覆')),
                ('creator', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('questionnaire', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='survey.Questionnaire')),
            ],
        ),
    ]

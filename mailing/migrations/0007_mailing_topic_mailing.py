# Generated by Django 4.2.2 on 2024-06-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0006_mailing_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='topic_mailing',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='название рассылки'),
        ),
    ]
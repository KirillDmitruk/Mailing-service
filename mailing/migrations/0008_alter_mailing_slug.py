# Generated by Django 4.2.2 on 2024-06-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0007_mailing_topic_mailing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='URL'),
        ),
    ]
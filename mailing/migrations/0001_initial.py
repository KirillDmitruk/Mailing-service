# Generated by Django 4.2.2 on 2024-06-05 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_start', models.DateTimeField(verbose_name='время начала рассылки')),
                ('datetime_finish', models.DateTimeField(verbose_name='время окончания рассылки')),
                ('period', models.CharField(choices=[('Единоразовая', 'Единоразовая'), ('Раз в день', 'Раз в день'), ('Раз в неделю', 'Раз в неделю'), ('Раз в месяц', 'Раз в месяц')], default='Раз в день', max_length=25, verbose_name='period')),
                ('status', models.CharField(choices=[('created', 'Создана'), ('started', 'Запущена'), ('finished', 'Завершена')], default='created', max_length=25, verbose_name='status')),
                ('clients', models.ManyToManyField(to='customers.customer', verbose_name='контакты клиентов')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='message.message', verbose_name='message')),
            ],
        ),
    ]
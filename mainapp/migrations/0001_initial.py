# Generated by Django 4.1.2 on 2022-10-07 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=80, verbose_name='Фамилия')),
                ('telegram', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телеграм номер или username')),
                ('phone_number', models.CharField(max_length=80, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Эл.Адрес')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]

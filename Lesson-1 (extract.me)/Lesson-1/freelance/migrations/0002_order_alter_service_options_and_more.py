# Generated by Django 5.0.3 on 2024-03-14 13:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('service', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='freelance.service', verbose_name='Услуга')),
                ('order_type', models.CharField(choices=[('design', 'Дизайн'), ('development', 'Разработка'), ('support', 'Поддержка')], default='design', max_length=11, verbose_name='Тип заказа')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='service',
            name='executor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelance.executor', verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_type',
            field=models.CharField(choices=[('design', 'Дизайн'), ('development', 'Разработка'), ('support', 'Поддержка')], default='design', max_length=11, verbose_name='Тип услуги'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='freelance.service', verbose_name='Услуга')),
            ],
        ),
    ]

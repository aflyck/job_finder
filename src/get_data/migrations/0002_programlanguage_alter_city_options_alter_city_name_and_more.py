# Generated by Django 4.0.6 on 2022-08-03 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Язык программирования')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Язык программирования',
                'verbose_name_plural': 'Языки программирования',
            },
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Наименование населенного пункта', 'verbose_name_plural': 'Наименование населенных пунктов'},
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Наименование населенного пункта'),
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
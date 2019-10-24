# Generated by Django 2.2.6 on 2019-10-23 05:26

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('company_name', models.TextField()),
                ('ingredient_list', django.contrib.postgres.fields.jsonb.JSONField()),
                ('heavy_metal', django.contrib.postgres.fields.jsonb.JSONField()),
                ('intake_hint', models.TextField()),
                ('intake_method', models.TextField()),
                ('preservation', models.TextField()),
                ('distrbution', models.TextField()),
                ('image_url', models.TextField()),
                ('views', models.IntegerField(default=0)),
                ('product_to_function', models.ManyToManyField(related_name='function_to_product', to='api.Function')),
                ('product_to_ingredient', models.ManyToManyField(related_name='ingredient_to_product', to='api.Ingredient')),
            ],
        ),
    ]

# Generated by Django 3.0.7 on 2020-08-15 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=150)),
                ('nutriscore_fr', models.CharField(max_length=2)),
                ('nutriscore_100g', models.CharField(max_length=150)),
                ('brands', models.CharField(max_length=150)),
                ('product_url', models.CharField(max_length=150)),
                ('image_nutrition', models.CharField(max_length=250)),
                ('image_food', models.CharField(max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['product_name'],
            },
        ),
        migrations.CreateModel(
            name='Substitute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
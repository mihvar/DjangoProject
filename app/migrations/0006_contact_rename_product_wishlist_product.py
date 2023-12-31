# Generated by Django 4.2.3 on 2023-07-31 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='wishlist',
            old_name='Product',
            new_name='product',
        ),
    ]

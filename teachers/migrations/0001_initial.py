# Generated by Django 3.2.5 on 2023-06-24 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default='media\\courses\x823\x06\x019\\default.png', upload_to='courses/%Y/%m/%d/')),
                ('facebook', models.URLField(blank=True, max_length=100)),
                ('twitter', models.URLField(blank=True, max_length=100)),
                ('linkedin', models.URLField(blank=True, max_length=100)),
                ('youtube', models.URLField(blank=True, max_length=100)),
            ],
        ),
    ]
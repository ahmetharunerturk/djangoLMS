# Generated by Django 3.2.5 on 2023-06-22 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.Tag'),
        ),
    ]

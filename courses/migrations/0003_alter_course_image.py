# Generated by Django 3.2.5 on 2023-06-19 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='courses/default_course_image.jpg', upload_to='courses/%Y/%m/%d/'),
        ),
    ]

# Generated by Django 3.2.5 on 2023-06-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='media/courses/images.png', upload_to='courses/%Y/%m/%d/'),
        ),
    ]
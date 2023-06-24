# Generated by Django 3.2.5 on 2023-06-24 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_teacher'),
        ('courses', '0010_course_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-25 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='video_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(upload_to='course-images'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='thumbnail',
            field=models.ImageField(upload_to='lesson-images'),
        ),
    ]
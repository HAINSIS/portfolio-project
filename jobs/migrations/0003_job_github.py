# Generated by Django 3.2.7 on 2021-10-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='github',
            field=models.URLField(default='#'),
        ),
    ]
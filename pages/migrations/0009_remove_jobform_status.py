# Generated by Django 5.0.5 on 2024-05-14 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_rename_jobs_jobform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobform',
            name='status',
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-19 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_content_task_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentheader',
            name='header_weight',
        ),
    ]

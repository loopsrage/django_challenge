# Generated by Django 3.0.3 on 2020-02-19 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20200219_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentheader',
            name='unique_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contentheader',
            name='header_text',
            field=models.TextField(),
        ),
    ]
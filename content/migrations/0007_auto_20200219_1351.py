# Generated by Django 3.0.3 on 2020-02-19 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_remove_contentheader_header_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentheader',
            name='content_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Content'),
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-22 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_text',
            field=models.TextField(default=0, max_length=4000),
            preserve_default=False,
        ),
    ]

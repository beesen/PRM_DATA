# Generated by Django 4.0.5 on 2022-06-22 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_item_display_direction'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='add_text_box_other',
            field=models.BooleanField(default=False),
        ),
    ]

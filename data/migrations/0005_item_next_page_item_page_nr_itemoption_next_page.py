# Generated by Django 4.0.5 on 2022-07-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_item_add_text_box_other'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='next_page',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='page_nr',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemoption',
            name='next_page',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
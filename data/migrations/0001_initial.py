# Generated by Django 4.0.5 on 2022-06-22 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
            options={
                'db_table': 'answer_types',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq_nr', models.IntegerField()),
                ('answer_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.answertype')),
            ],
            options={
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('has_options', models.BooleanField(default=False)),
                ('has_statements', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'item_types',
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
            options={
                'db_table': 'surveys',
            },
        ),
        migrations.CreateModel(
            name='ItemStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq_nr', models.IntegerField()),
                ('statement_text', models.CharField(max_length=256)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.item')),
            ],
            options={
                'db_table': 'item_statements',
            },
        ),
        migrations.CreateModel(
            name='ItemOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq_nr', models.IntegerField()),
                ('option_text', models.CharField(max_length=256)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.item')),
            ],
            options={
                'db_table': 'item_options',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.itemtype'),
        ),
        migrations.AddField(
            model_name='item',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.survey'),
        ),
    ]
# Generated by Django 4.1.5 on 2023-01-08 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_rename_desc_facts_main_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skill6_t',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill6_v',
            field=models.IntegerField(null=True),
        ),
    ]

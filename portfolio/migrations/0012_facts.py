# Generated by Django 4.1.5 on 2023-01-07 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_about_image_alter_about_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True, max_length=450, null=True)),
                ('happyclients', models.IntegerField(blank=True, null=True)),
                ('Projects', models.IntegerField(blank=True, null=True)),
                ('Support', models.IntegerField(blank=True, null=True)),
                ('Hardworks', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
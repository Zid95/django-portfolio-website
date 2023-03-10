# Generated by Django 4.1.5 on 2023-01-06 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Self',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('twitter', models.URLField(blank=True, max_length=100, null=True)),
                ('facebook', models.URLField(blank=True, max_length=100, null=True)),
                ('instagram', models.URLField(blank=True, max_length=100, null=True)),
                ('skype', models.URLField(blank=True, max_length=100, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=100, null=True)),
                ('skill1', models.CharField(blank=True, max_length=30, null=True)),
                ('skill2', models.CharField(blank=True, max_length=30, null=True)),
                ('skill3', models.CharField(blank=True, max_length=30, null=True)),
                ('skill4', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-08 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_services'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facts',
            old_name='desc',
            new_name='main_desc',
        ),
        migrations.RenameField(
            model_name='facts',
            old_name='Hardworks',
            new_name='total1',
        ),
        migrations.RenameField(
            model_name='facts',
            old_name='Projects',
            new_name='total2',
        ),
        migrations.RenameField(
            model_name='facts',
            old_name='Support',
            new_name='total3',
        ),
        migrations.RenameField(
            model_name='facts',
            old_name='happyclients',
            new_name='total4',
        ),
        migrations.AddField(
            model_name='facts',
            name='desc1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='facts',
            name='desc2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='facts',
            name='desc3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='facts',
            name='desc4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='facts',
            name='title1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='facts',
            name='title2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='facts',
            name='title3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='facts',
            name='title4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
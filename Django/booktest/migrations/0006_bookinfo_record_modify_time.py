# Generated by Django 3.2 on 2022-08-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0005_alter_bookinfo_bpub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='record_modify_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
# Generated by Django 3.2 on 2022-08-24 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0008_alter_heroinfo_hname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='hcomment',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

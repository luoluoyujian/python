# Generated by Django 3.2 on 2022-08-25 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0011_alter_heroinfo_hbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=20)),
                ('type_news', models.ManyToManyField(to='booktest.NewsInfo')),
            ],
        ),
    ]

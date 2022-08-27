# Generated by Django 3.2 on 2022-08-25 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0012_newsinfo_newstype'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeBasicInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.BooleanField(default=False)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDetailInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=256)),
                ('employee_basic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booktest.employeebasicinfo')),
            ],
        ),
    ]

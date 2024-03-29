# Generated by Django 2.1.7 on 2019-03-06 08:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20190306_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpensesReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(default=datetime.datetime(2019, 3, 6, 8, 36, 45, 695941, tzinfo=utc))),
                ('Name', models.CharField(default='name', max_length=100, null=True)),
                ('Reason', models.CharField(default='reason', max_length=100, null=True)),
                ('Amount', models.FloatField(verbose_name=0.0)),
            ],
        ),
        migrations.AlterField(
            model_name='expensesreportarchive',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 6, 8, 36, 45, 695941, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='salary',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 6, 8, 36, 45, 694944, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spend',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 6, 8, 36, 45, 695941, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sundry',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 6, 8, 36, 45, 695941, tzinfo=utc)),
        ),
    ]

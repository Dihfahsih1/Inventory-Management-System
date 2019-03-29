# Generated by Django 2.1.7 on 2019-03-09 06:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_auto_20190309_0831'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryReportArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(default=datetime.datetime(2019, 3, 9, 6, 43, 48, 703377, tzinfo=utc))),
                ('Salary_Type', models.CharField(max_length=100, null=True)),
                ('Staff', models.CharField(max_length=100, null=True)),
                ('Month', models.CharField(max_length=100, null=True)),
                ('Amount', models.IntegerField(default=0)),
                ('archivedmonth', models.CharField(max_length=100, null=True)),
                ('archivedyear', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ExpensesReport',
        ),
        migrations.AlterField(
            model_name='expensesreportarchive',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 9, 6, 43, 48, 702381, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='salary',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 9, 6, 43, 48, 700385, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spend',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 9, 6, 43, 48, 702381, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sundry',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 9, 6, 43, 48, 701383, tzinfo=utc)),
        ),
    ]

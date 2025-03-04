# Generated by Django 3.2.25 on 2024-07-05 18:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Applicant',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='skills_required',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='work_format',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='city',
            field=models.CharField(default='2024-07-05 18:48:32.906748+00:00', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='currency',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='employer_name',
            field=models.CharField(default='Unknown Employer', max_length=255),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 5, 18, 51, 46, 112071, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='requirements',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='responsibilities',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='salary_from',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='salary_to',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.1 on 2022-08-30 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='report_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
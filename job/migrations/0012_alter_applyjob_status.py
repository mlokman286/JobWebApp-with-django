# Generated by Django 5.0 on 2023-12-31 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_alter_applyjob_status_alter_job_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Declined', 'Declinned'), ('Accepted', 'Accepted')], max_length=100),
        ),
    ]

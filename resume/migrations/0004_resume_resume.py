# Generated by Django 5.0 on 2023-12-31 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_rename_loaction_resume_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resume'),
        ),
    ]

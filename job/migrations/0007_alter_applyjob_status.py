# Generated by Django 5.0 on 2023-12-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_applyjob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Declined', 'Declinned'), ('Pending', 'Pending')], max_length=100),
        ),
    ]
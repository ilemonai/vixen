# Generated by Django 4.1 on 2022-11-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosmetic_site', '0003_payment_alter_appointment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]

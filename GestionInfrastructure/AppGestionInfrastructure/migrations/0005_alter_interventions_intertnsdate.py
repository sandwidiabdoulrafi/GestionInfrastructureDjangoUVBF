# Generated by Django 5.1.1 on 2024-10-07 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGestionInfrastructure', '0004_alter_infrastructures_id_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interventions',
            name='intertnsDate',
            field=models.DateField(null=True),
        ),
    ]

# Generated by Django 5.0 on 2024-05-19 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riskscoreapp', '0007_alter_cancerdb_m_substanceabuse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancerdb',
            name='m_Patient_name',
            field=models.CharField(default='Unknown', max_length=25),
        ),
    ]

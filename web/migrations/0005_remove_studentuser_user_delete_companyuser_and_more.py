# Generated by Django 4.1.5 on 2023-01-18 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_studentuser_companyuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='CompanyUser',
        ),
        migrations.DeleteModel(
            name='StudentUser',
        ),
    ]
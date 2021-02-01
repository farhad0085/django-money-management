# Generated by Django 3.1.4 on 2021-02-01 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_auto_20210201_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('earn', 'Earn'), ('spend', 'Spend')], default='spend', max_length=10),
        ),
    ]

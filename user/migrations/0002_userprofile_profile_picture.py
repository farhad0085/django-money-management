# Generated by Django 3.1.4 on 2021-01-31 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='', upload_to='images/dp'),
            preserve_default=False,
        ),
    ]
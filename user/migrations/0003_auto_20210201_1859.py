# Generated by Django 3.1.4 on 2021-02-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(upload_to='%Y/%B/%d/images/dp'),
        ),
    ]

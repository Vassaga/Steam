# Generated by Django 4.2.3 on 2023-07-25 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_alter_invitecard_expiration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='screen',
            name='screen_image',
            field=models.ImageField(default='games/unknown.png', upload_to='games/', verbose_name='скрин'),
        ),
        migrations.AlterField(
            model_name='invitecard',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 24, 19, 50, 32, 288046), verbose_name='дата истечения'),
        ),
    ]
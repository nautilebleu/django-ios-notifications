# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ios_notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='service',
            field=models.ForeignKey(default=1, to='ios_notifications.APNService'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='users',
            field=models.ManyToManyField(related_name='ios_devices', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]

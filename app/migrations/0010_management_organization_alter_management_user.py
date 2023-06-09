# Generated by Django 4.0.2 on 2023-04-01 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_user_is_agent_user_is_organisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='management',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.userprofile'),
        ),
        migrations.AlterField(
            model_name='management',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]

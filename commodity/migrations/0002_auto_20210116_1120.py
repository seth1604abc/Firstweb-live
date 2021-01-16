# Generated by Django 3.1.5 on 2021-01-16 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commodity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='iframe',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='music',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.singer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=phone_field.models.PhoneField(max_length=31),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.commodity'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 2.2 on 2020-10-17 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('church', '0001_initial'),
        ('Job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='church',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.Church'),
        ),
    ]

# Generated by Django 2.2 on 2020-10-12 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('church', '0002_church_user'),
        ('user', '0002_auto_20201011_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_item', models.CharField(help_text='Category', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('duration', models.CharField(choices=[('Once', 'One Time'), ('Long', 'Long-term')], default='Once', max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('body', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Job.Category')),
                ('church', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.Church')),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_submitted', models.DateField(auto_now_add=True)),
                ('timeframe', models.CharField(choices=[('One week', 'Less than 1 week'), ('One month', 'Less than 1 month'), ('three months', '1 to 3 months'), ('three and up', 'More than 3 months')], default='One week', max_length=20)),
                ('body', models.TextField()),
                ('files', models.FileField(blank=True, null=True, upload_to='attachments/')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Job.Job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Volunteer')),
            ],
        ),
    ]

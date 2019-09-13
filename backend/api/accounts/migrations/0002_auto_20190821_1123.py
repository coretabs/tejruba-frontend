# Generated by Django 2.2.4 on 2019-08-21 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='settings',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.Settings'),
            preserve_default=False,
        ),
    ]

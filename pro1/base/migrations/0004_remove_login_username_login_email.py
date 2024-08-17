# Generated by Django 5.1 on 2024-08-16 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_login_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='username',
        ),
        migrations.AddField(
            model_name='login',
            name='email',
            field=models.EmailField(default='Provide a one-off default now', max_length=200),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.3 on 2024-05-02 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customuser_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='favorite',
        ),
    ]

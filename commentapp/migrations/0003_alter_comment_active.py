# Generated by Django 4.1.4 on 2022-12-12 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0002_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

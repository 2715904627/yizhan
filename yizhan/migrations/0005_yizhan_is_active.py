# Generated by Django 4.1.7 on 2023-03-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yizhan', '0004_alter_yizhan_na_en_alter_yizhan_na_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='yizhan',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

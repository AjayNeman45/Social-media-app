# Generated by Django 3.2.5 on 2021-09-29 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapi', '0011_auto_20210928_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(max_length=500),
        ),
    ]

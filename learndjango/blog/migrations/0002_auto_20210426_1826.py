# Generated by Django 3.2 on 2021-04-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='description',
            new_name='content',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]

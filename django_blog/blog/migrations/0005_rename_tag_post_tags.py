# Generated by Django 5.1.6 on 2025-03-21 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_tag_delete_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
    ]

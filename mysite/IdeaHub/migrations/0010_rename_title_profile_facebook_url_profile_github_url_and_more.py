# Generated by Django 5.0.2 on 2024-02-08 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IdeaHub', '0009_profile_profile_picture_profile_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='title',
            new_name='facebook_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='github_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='website_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
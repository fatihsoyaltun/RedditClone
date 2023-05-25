# Generated by Django 4.1.7 on 2023-05-25 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_backimage_profile_bio_profile_created_at_and_more'),
        ('posts', '0007_alter_post_grup'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislike',
            field=models.ManyToManyField(blank=True, null=True, related_name='dislikes', to='user.profile', verbose_name='Begenmeyenler'),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, to='user.profile', verbose_name='Begenenler'),
        ),
    ]
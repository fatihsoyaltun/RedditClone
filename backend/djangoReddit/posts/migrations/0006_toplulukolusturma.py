# Generated by Django 4.2 on 2023-05-24 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toplulukolusturma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toplulukadı', models.CharField(max_length=100, null=True)),
                ('toplulukbackgroundimg', models.FileField(blank=True, null=True, upload_to='posts/')),
                ('toplulukprofileimg', models.FileField(blank=True, null=True, upload_to='posts/')),
            ],
        ),
    ]

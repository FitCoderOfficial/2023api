# Generated by Django 4.1.5 on 2023-01-10 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_review_date_created_review_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='img'),
        ),
    ]

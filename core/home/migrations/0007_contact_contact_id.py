# Generated by Django 5.1.5 on 2025-02-22 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_contact_age_remove_contact_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

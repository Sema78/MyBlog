# Generated by Django 4.1.6 on 2023-02-12 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0003_category_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_category_title_alter_news_columns_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_columns',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
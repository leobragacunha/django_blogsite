# Generated by Django 4.1 on 2024-04-03 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_comment_comment_blogger_comment_updated_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="updated_date",
            field=models.DateTimeField(verbose_name="Updated on"),
        ),
        migrations.AlterField(
            model_name="post",
            name="updated_date",
            field=models.DateTimeField(verbose_name="Updated on"),
        ),
    ]
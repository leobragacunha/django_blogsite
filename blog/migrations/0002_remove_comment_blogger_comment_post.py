# Generated by Django 4.1 on 2024-03-30 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="blogger",
        ),
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="blog.post"
            ),
        ),
    ]

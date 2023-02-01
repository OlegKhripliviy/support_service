# Generated by Django 4.1.5 on 2023-02-01 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0001_initial"),
        ("comments", "0003_alter_comment_prev_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="ticket",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="tickets.ticket",
            ),
        ),
    ]

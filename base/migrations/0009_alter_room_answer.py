# Generated by Django 4.1.9 on 2023-09-30 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_room_answer_alter_room_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='answer',
            field=models.CharField(blank=True, default=' ', max_length=255, null=True),
        ),
    ]

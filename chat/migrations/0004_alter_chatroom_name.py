# Generated by Django 4.0.2 on 2022-03-07 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_chatroom_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_category_alter_person_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='categories',
            field=models.ManyToManyField(to='todos.category'),
        ),
    ]

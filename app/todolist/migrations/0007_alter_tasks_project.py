# Generated by Django 4.1.2 on 2022-10-13 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_project_is_deleted_tasks_is_deleted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todolist.project', verbose_name='Проект'),
        ),
    ]

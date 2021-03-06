# Generated by Django 4.0.4 on 2022-07-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager_app', '0005_task_created_at_task_due_date_task_percentage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='phase',
            field=models.CharField(choices=[('TODO', 'TODO'), ('DOING', 'DOING'), ('DONE ', 'DONE')], default='TODO', max_length=5),
        ),
        migrations.AddField(
            model_name='task',
            name='row_position',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]

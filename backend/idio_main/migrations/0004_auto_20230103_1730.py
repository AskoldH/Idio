# Generated by Django 3.2 on 2023-01-03 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idio_main', '0003_idiouser_last_edu_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='idiouser',
            name='next_edu_video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='next_edu_video', to='idio_main.eduvideo'),
        ),
        migrations.AlterField(
            model_name='idiouser',
            name='last_edu_video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='last_edu_video', to='idio_main.eduvideo'),
        ),
    ]

# Generated by Django 3.2 on 2022-05-25 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ekklesia_shared', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitytype',
            name='insert_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='activity_type_insert_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='update_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='activity_type_update_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='asset',
            name='insert_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='asset_insert_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='asset',
            name='update_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='asset_update_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entitytype',
            name='insert_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='entity_type_insert_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entitytype',
            name='update_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='entity_type_update_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movementtype',
            name='insert_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='movement_type_insert_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movementtype',
            name='update_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='movement_type_update_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='position',
            name='insert_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='position_insert_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='position',
            name='update_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='position_update_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

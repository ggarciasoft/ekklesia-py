# Generated by Django 3.2 on 2022-05-25 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ekklesia_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='insert_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='activity_insert_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activity',
            name='update_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='activity_update_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activityassistant',
            name='insert_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='activity_assistant_insert_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activityassistant',
            name='update_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='activity_assistant_update_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contact',
            name='insert_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contact_insert_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contact',
            name='update_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='contact_update_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ministry',
            name='insert_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ministry_insert_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ministry',
            name='update_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ministry_update_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movement',
            name='insert_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='movement_insert_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movement',
            name='update_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='movement_update_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movementdetail',
            name='insert_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='movement_detail_insert_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movementdetail',
            name='update_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='movement_detail_update_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

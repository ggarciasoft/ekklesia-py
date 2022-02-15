# Generated by Django 4.0 on 2022-02-15 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_date', models.DateField()),
                ('comments', models.CharField(max_length=500, null=True)),
                ('insert_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('is_active', models.BooleanField()),
                ('insert_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(null=True)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='asset_insert_user', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('home_phone', models.CharField(max_length=10, null=True)),
                ('cell_phone', models.CharField(max_length=10, null=True)),
                ('is_local_member', models.BooleanField()),
                ('birth_date', models.DateField(null=True)),
                ('conversion_date', models.DateField(null=True)),
                ('baptism_date', models.DateField(null=True)),
                ('contact_image', models.ImageField(null=True, upload_to='')),
                ('is_active', models.BooleanField()),
                ('insert_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(null=True)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contact_insert_user', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_date', models.DateTimeField()),
                ('comments', models.CharField(max_length=500, null=True)),
                ('insert_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(null=True)),
                ('activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.activity')),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='movement_insert_user', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserTenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.tenant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('is_active', models.BooleanField()),
                ('insert_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(null=True)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='position_insert_user', to='auth.user')),
                ('tenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.tenant')),
                ('update_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='position_update_user', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='MovementType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('is_active', models.BooleanField()),
                ('insert_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(null=True)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='movement_type_insert_user', to='auth.user')),
                ('tenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.tenant')),
                ('update_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='movement_type_update_user', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='MovementDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_quantity', models.FloatField()),
                ('comments', models.CharField(max_length=500, null=True)),
                ('insert_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.asset')),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.contact')),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='movement_detail_insert_user', to='auth.user')),
                ('movement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.movement')),
                ('movement_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.movementtype')),
                ('update_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='movement_detail_update_user', to='auth.user')),
            ],
        ),
        migrations.AddField(
            model_name='movement',
            name='tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.tenant'),
        ),
        migrations.AddField(
            model_name='movement',
            name='update_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='movement_update_user', to='auth.user'),
        ),
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('is_active', models.BooleanField()),
                ('insert_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(null=True)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ministry_insert_user', to='auth.user')),
                ('tenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.tenant')),
                ('update_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ministry_update_user', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='MemberMinistryPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.contact')),
                ('ministry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.ministry')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.position')),
            ],
        ),
        migrations.CreateModel(
            name='EntityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('is_active', models.BooleanField()),
                ('insert_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(null=True)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='entity_type_insert_user', to='auth.user')),
                ('tenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.tenant')),
                ('update_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='entity_type_update_user', to='auth.user')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.tenant'),
        ),
        migrations.AddField(
            model_name='contact',
            name='update_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='contact_update_user', to='auth.user'),
        ),
        migrations.AddField(
            model_name='asset',
            name='tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.tenant'),
        ),
        migrations.AddField(
            model_name='asset',
            name='update_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='asset_update_user', to='auth.user'),
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('is_active', models.BooleanField()),
                ('insert_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(null=True)),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='activity_type_insert_user', to='auth.user')),
                ('tenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.tenant')),
                ('update_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='activity_type_update_user', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityAssistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=500, null=True)),
                ('insert_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.activity')),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.contact')),
                ('entity_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekklesia_main.entitytype')),
                ('insert_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='activity_assistant_insert_user', to='auth.user')),
                ('update_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='activity_assistant_update_user', to='auth.user')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ekklesia_main.activitytype'),
        ),
        migrations.AddField(
            model_name='activity',
            name='insert_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='activity_insert_user', to='auth.user'),
        ),
        migrations.AddField(
            model_name='activity',
            name='tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ekklesia_main.tenant'),
        ),
        migrations.AddField(
            model_name='activity',
            name='update_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='activity_update_user', to='auth.user'),
        ),
    ]

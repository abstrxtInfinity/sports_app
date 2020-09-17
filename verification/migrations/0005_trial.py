# Generated by Django 3.1.1 on 2020-09-17 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0004_delete_user_certificates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('venue', models.CharField(max_length=256)),
                ('no_of_selections', models.PositiveIntegerField(default=5)),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=256)),
                ('min_height', models.PositiveIntegerField()),
                ('max_height', models.PositiveIntegerField()),
                ('min_weight', models.PositiveIntegerField()),
                ('max_weight', models.PositiveIntegerField()),
                ('age_group', models.CharField(max_length=256)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='verification.sport')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='verification.state')),
            ],
        ),
    ]
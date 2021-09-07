# Generated by Django 3.2.7 on 2021-09-06 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travelname', models.CharField(max_length=100)),
                ('returndate', models.DateField()),
                ('durationoftravel', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=100)),
                ('ispacked', models.BooleanField(default=False)),
                ('priority', models.CharField(blank=True, choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], max_length=10)),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.travel')),
            ],
        ),
    ]
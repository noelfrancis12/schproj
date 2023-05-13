# Generated by Django 4.2 on 2023-05-11 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usermember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('number', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schapp.course')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

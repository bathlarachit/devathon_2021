# Generated by Django 3.0.5 on 2021-09-19 07:24

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
            name='Application',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('birthdate', models.DateField()),
                ('aadhar', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
                ('gender', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=20)),
                ('specialization', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
                ('documents', models.FileField(default='', upload_to='student/pdf')),
                ('photo', models.ImageField(default='', upload_to='student/images')),
                ('notes', models.CharField(max_length=255)),
                ('submitted', models.CharField(max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

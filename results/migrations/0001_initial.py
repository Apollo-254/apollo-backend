# Generated by Django 4.2.2 on 2023-06-29 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('results_report', models.FileField(default='', upload_to='uploads/')),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('lab_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lab_results', to='labs.lab')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_results', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

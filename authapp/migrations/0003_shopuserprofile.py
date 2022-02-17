# Generated by Django 3.2 on 2021-12-27 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20211225_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(blank=True, max_length=128, null=True)),
                ('about_me', models.TextField(blank=True, max_length=512, null=True)),
                ('gender', models.CharField(choices=[('M', 'М'), ('F', 'Ж'), ('U', 'Н')], default='U', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

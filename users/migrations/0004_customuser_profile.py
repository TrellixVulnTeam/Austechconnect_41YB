# Generated by Django 2.2.1 on 2019-06-05 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_remove_person_user'),
        ('users', '0003_remove_customuser_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='search.Person'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-14 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210414_1839'),
        ('comments', '0002_auto_20210414_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userprofile'),
        ),
    ]
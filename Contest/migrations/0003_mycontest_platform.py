# Generated by Django 3.2 on 2021-05-10 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contest', '0002_mycontest_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycontest',
            name='platform',
            field=models.CharField(choices=[('CF', 'Codeforces'), ('CC', 'Codechef'), ('AC', 'Atcoder')], default='CF', max_length=20),
        ),
    ]

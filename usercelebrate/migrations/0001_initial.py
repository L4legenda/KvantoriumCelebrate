# Generated by Django 3.0.3 on 2020-07-07 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('visit', models.IntegerField(choices=[(0, 'Ушел'), (1, 'Пришел')], max_length=1)),
                ('children', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userlist.Children')),
            ],
        ),
    ]

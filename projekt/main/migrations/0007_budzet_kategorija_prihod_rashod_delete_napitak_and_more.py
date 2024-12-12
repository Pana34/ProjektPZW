# Generated by Django 5.1.2 on 2024-11-27 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_napitak_id_alter_sladoled_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budzet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=30)),
                ('iznos', models.FloatField()),
                ('datum', models.DateField()),
                ('opis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Kategorija',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=30)),
                ('opis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Prihod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=30)),
                ('iznos', models.FloatField()),
                ('datum', models.DateField()),
                ('opis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rashod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=30)),
                ('iznos', models.FloatField()),
                ('datum', models.DateField()),
                ('opis', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Napitak',
        ),
        migrations.RemoveField(
            model_name='sladoledni_kup',
            name='sladoled',
        ),
        migrations.DeleteModel(
            name='Sladoled',
        ),
        migrations.DeleteModel(
            name='Sladoledni_kup',
        ),
    ]
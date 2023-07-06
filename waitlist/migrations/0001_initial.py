# Generated by Django 4.2.3 on 2023-07-05 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waitlist.useremail')),
            ],
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=255)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waitlist.useremail')),
            ],
        ),
        migrations.AddField(
            model_name='useremail',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='waitlist.username'),
        ),
    ]

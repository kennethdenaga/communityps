# Generated by Django 3.1.6 on 2021-06-03 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kenlist', '0004_auto_20210503_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation', models.TextField(max_length=50)),
                ('donation_type', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Donator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('contactnumber', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=50)),
                ('location', models.TextField(max_length=50)),
                ('donation', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='kenlist.donation')),
            ],
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recname', models.DateField(max_length=50)),
                ('rec_contactnumber', models.TextField(max_length=50)),
                ('donation', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='kenlist.donation')),
            ],
        ),
        migrations.CreateModel(
            name='Remarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(default='', max_length=50)),
                ('remarks', models.TextField(default='', max_length=50)),
                ('donation', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='kenlist.donation')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='List',
        ),
        migrations.AddField(
            model_name='donation',
            name='donator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='kenlist.donator'),
        ),
    ]

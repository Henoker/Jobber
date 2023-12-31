# Generated by Django 4.0 on 2023-10-10 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('interview', 'Interview'), ('declined', 'Declined'), ('pending', 'Pending')], default='pending', max_length=10)),
                ('job_type', models.CharField(choices=[('full-time', 'Full-time'), ('part-time', 'Part-time'), ('remote', 'Remote'), ('internship', 'Internship')], default='full-time', max_length=20)),
                ('job_location', models.CharField(default='my city', max_length=100)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
        ),
    ]

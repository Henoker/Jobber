from django.db import models  
from accounts.models import CustomUser

# Create your models here.
class Job(models.Model):
    company = models.CharField(blank=False, null=False, max_length=50)
    position = models.CharField(blank=False, null=False, max_length=100)
    status_choices = [
        ('interview', 'Interview'),
        ('declined', 'Declined'),
        ('pending', 'Pending')
    ]
    status = models.CharField(
        max_length=10,
        choices=status_choices,
        default='pending'
    )
    job_type_choices = [
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('remote', 'Remote'),
        ('internship', 'Internship')
    ]
    job_type = models.CharField(
        max_length=20,
        choices=job_type_choices,
        default='full-time'
    )
    job_location = models.CharField(blank=False, null=False, max_length=100, default='my city')
    created_by = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
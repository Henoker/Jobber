from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Job

class JobTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )
        cls.job = Job.objects.create(
            created_by=cls.user,
            company="ABC corporation",
            position="Junior Software Developer",
            status ="pending",
            job_type="full-time",
            job_location="Nairobi",
        )
def test_job_model(self):
    self.assertEqual(self.job.created_by.username, "testuser")
    self.assertEqual(self.job.company, "ABC corporation")
    self.assertEqual(self.job.position, "Junior Software Developer")
    self.assertEqual(self.job.status, "pending")
    self.assertEqual(self.job_type, "full-time")
    self.assertEqual(self.job_location, "Nairobi")
   
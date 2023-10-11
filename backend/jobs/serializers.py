from  rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
           "company",
           "position",
           "status",
           "job_type",
           "job_location",
           "created_by",
        )
        model = Job
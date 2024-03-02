from django.db import models

# Create your models here.
class Company(models.Model):

    cname = models.CharField(max_length=100)


class Userdetails(models.Model):

    name = models.CharField(max_length=100)
    linkedin_url = models.URLField(blank=True, null=True)
    branch = models.CharField(max_length=50)
    rollno = models.CharField(max_length=20)
    year_of_passout = models.IntegerField()
    email = models.EmailField()
    contact_no = models.CharField(max_length=15, blank=True, null=True)


class Interview(models.Model):

    user = models.ForeignKey(Userdetails, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    year_of_interview = models.IntegerField()
    role = models.CharField(max_length=100)
    brief_description = models.TextField(blank=True, null=True)
    selection_procedure = models.TextField()
    online_test_desc = models.TextField(blank=True, null=True)
    tech_interview_desc = models.TextField()
    hr_interview_desc = models.TextField()
    prep_resources = models.TextField(blank=True, null=True)
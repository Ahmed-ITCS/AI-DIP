from django.db import models
from student.models import Skill  # Importing the Skill and Internship models from another app
from student.models import User


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=200)  # You can adjust the max_length as per your requirement
    
    def __str__(self):
        return self.name


class Internship(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirement = models.TextField()
    is_ai_driven = models.BooleanField(default=False)
    organizationid= models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title
    
class AIProblem(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField()
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True)
    internshipid = models.ForeignKey(Internship, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.type} Problem"
    

class InternshipApplication(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    internshipid = models.ForeignKey(Internship, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)  # Corrected field type to CharField

    def __str__(self):
        return f"Application #{self.id} - {self.user.username} for {self.internship.title}"
    

class Certification(models.Model):
    id = models.AutoField(primary_key=True)
    issue_date = models.DateField()
    studentid = models.ForeignKey(User, on_delete=models.CASCADE)
    internshipid = models.ForeignKey(Organization, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Certification #{self.id}"
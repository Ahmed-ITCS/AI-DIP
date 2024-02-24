from django.contrib.postgres.fields import ArrayField
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # You should use more secure methods to store passwords
    skills = ArrayField(models.CharField(max_length=100), blank=True)
    assessment = ArrayField(models.CharField(max_length=100), blank=True)

class SkillAssessment(models.Model):
    id = models.AutoField(primary_key=True)
    proficiency_score = models.IntegerField()
    proficiency_level = models.CharField(max_length=50)
    studentid = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f"Skill Assessment for {self.student.name}"
    

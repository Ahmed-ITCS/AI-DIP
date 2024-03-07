from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # You should use more secure methods to store passwords

class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class SkillAssessment(models.Model):
    id = models.AutoField(primary_key=True)
    proficiency_score = models.IntegerField()
    proficiency_level = models.CharField(max_length=50)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"Skill Assessment for {self.user.name}"
    
class AIManager(models.Model):
    id = models.AutoField(primary_key=True)
    problem_id = models.CharField(max_length=100)

    def __str__(self):
        return f"AIManager ID: {self.id}, Problem ID: {self.problem_id}"

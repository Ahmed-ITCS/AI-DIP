from django.contrib import admin
from student.models import SkillAssessment
from student.models import User

# Register your models here.
admin.site.register(SkillAssessment)
admin.site.register(User)

from django.contrib import admin
from student.models import SkillAssessment
from student.models import User
from student.models import AIManager
from student.models import Skill

# Register your models here.
admin.site.register(Skill)
admin.site.register(SkillAssessment)
admin.site.register(User)
admin.site.register(AIManager)


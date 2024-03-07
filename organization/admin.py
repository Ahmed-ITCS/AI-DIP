from django.contrib import admin

from organization.models import Organization
from organization.models import Internship
from organization.models import AIProblem
from organization.models import InternshipApplication
from organization.models import Certification

# Register your models here.
admin.site.register(Organization)
admin.site.register(Internship)
admin.site.register(AIProblem)
admin.site.register(InternshipApplication)
admin.site.register(Certification)
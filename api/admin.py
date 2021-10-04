from django.contrib import admin

from api.models import Alumni, Blog, Gallery, Project, TeamModel, Workshop

# Register your models here.
admin.site.register(TeamModel)
admin.site.register(Blog)
admin.site.register(Workshop)
admin.site.register(Alumni)
admin.site.register(Gallery)
admin.site.register(Project)

from django.contrib import admin

from api.models import Alumni, Blog, TeamModel, Workshop

# Register your models here.
admin.site.register(TeamModel)
admin.site.register(Blog)
admin.site.register(Workshop)
admin.site.register(Alumni)

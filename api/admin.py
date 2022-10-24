from django.contrib import admin

from api.models import Alumni
from api.models import Attendees
from api.models import Gallery
from api.models import MemberRegistration
from api.models import Project
from api.models import TeamModel
from api.models import Workshop


class TeamModelFilter(admin.ModelAdmin):
    list_display = ["name", "title", "github_id", "linkedin_id"]
    list_filter = ["title"]
    search_fields = ["name"]


admin.site.register(TeamModel, TeamModelFilter)


class WorkshopFilter(admin.ModelAdmin):
    list_display = ["title", "event_date", "venue"]
    list_filter = ["title", "event_date"]
    search_fields = ["title", "venue"]


admin.site.register(Workshop, WorkshopFilter)


class GalleryFilter(admin.ModelAdmin):
    list_display = ["event", "sub_event", "year"]
    list_filter = ["event", "year"]


admin.site.register(Gallery, GalleryFilter)


class AlumniFilter(admin.ModelAdmin):
    list_display = ["name", "batch", "company"]
    list_filter = ["batch", "dual_degree"]
    search_fields = ["name"]


admin.site.register(Alumni, AlumniFilter)


class ProjectFilter(admin.ModelAdmin):
    list_display = ["domain", "name", "year", "github_link"]
    list_filter = ["domain", "year"]
    search_fields = ["name"]


admin.site.register(Project, ProjectFilter)


class MemberRegistrationFilter(admin.ModelAdmin):
    list_display = ["name", "roll_no", "degree", "branch"]
    list_filter = ["name", "degree", "branch"]
    search_fields = ["name", "degree", "branch"]


admin.site.register(MemberRegistration, MemberRegistrationFilter)


class AttendeesAdmin(admin.ModelAdmin):
    list_display = ["email", "name", "workshop"]
    search_fields = ["email", "name"]


admin.site.register(Attendees, AttendeesAdmin)

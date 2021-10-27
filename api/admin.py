from django.contrib import admin

from api.models import Alumni, Gallery, Project, TeamModel, Workshop


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

from datetime import datetime

from django.core import serializers
from django.http.response import HttpResponseBadRequest
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import TemplateView

from api import models
from api.forms import GalleryForm
from api.forms import WorkshopForm


def dump_data(request):
    all_objects = [
        *models.TeamModel.objects.all(),
        *models.Workshop.objects.all(),
        *models.Gallery.objects.all(),
        *models.Alumni.objects.all(),
        *models.Project.objects.all(),
    ]
    data = serializers.serialize("json", all_objects, indent=2)
    extension = ".json"
    filename = datetime.now().strftime("%Y%m%d-%H%M%S") + extension
    response = HttpResponse(data, content_type="application/json")
    response["Content-Disposition"] = "attachment; filename=" + filename
    return response


def GalleryFormView(request):
    context = {}
    if request.method == "POST":
        upload_files = request.FILES.getlist("image")
        for file in upload_files:
            formset = GalleryForm(request.POST, {"image": file})
            if formset.is_valid():
                formset.save()
                return HttpResponse("Success")

            else:
                return HttpResponseBadRequest(formset.errors)

    context["form"] = GalleryForm()
    return render(request, "gallery.html", context)


def WorkshopFormView(request):
    context = {}
    if request.method == "POST":
        form = WorkshopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context["message"] = "Successful"

        else:
            context["error"] = form.errors

    context["form"] = WorkshopForm()
    return render(request, "workshop.html", context)


class Home(TemplateView):
    template_name = "home.html"


class TeamModelCreateView(CreateView):
    model = models.TeamModel
    fields = ["name", "title", "github_id", "linkedin_id", "profile_pic"]
    template_name = "team.html"
    success_url = "/"


class AlumniCreateView(CreateView):
    model = models.Alumni
    fields = [
        "name",
        "batch",
        "dual_degree",
        "company",
        "github_id",
        "linkedin_id",
        "profile_pic",
    ]
    template_name = "alumni.html"
    success_url = "/"


class ProjectCreateView(CreateView):
    model = models.Project
    fields = ["domain", "name", "year", "description", "github_link", "cover"]
    template_name = "project.html"
    success_url = "/"

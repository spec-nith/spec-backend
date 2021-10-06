from datetime import datetime

from django.shortcuts import HttpResponse, render
from django.utils.timezone import make_aware
from django.views.generic import TemplateView, base

from api import models
from api.forms import GalleryForm


def GalleryFormView(request):
    context = {}
    if request.method == "POST":
        upload_files = request.FILES.getlist("image")
        for file in upload_files:
            formset = GalleryForm(request.POST, {"image": file})
            if formset.is_valid():
                formset.save()
                context["message"] = "Successful"

            else:
                context["error"] = formset.errors

    context["form"] = GalleryForm()
    return render(request, "gallery.html", context)


class Home(TemplateView):
    template_name = "home.html"


class URLUpdateView(base.View):
    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            try:
                last_access = models.AccessModel.objects.all().last().time
            except AttributeError:
                last_access = make_aware(
                    datetime.strptime("2001-01-01 01:01:01", "%Y-%m-%d %H:%M:%S")
                )

            curr = make_aware(datetime.now())
            if (curr - last_access).total_seconds() < 1 * 60 * 60:
                return HttpResponse("Indexing Requested Too Fast")

        for i in models.TeamModel.objects.all():
            i.update_team_image_url()

        for i in models.Blog.objects.all():
            i.update_blog_cover_url()

        for i in models.Workshop.objects.all():
            i.update_workshop_cover_url()

        for i in models.Gallery.objects.all():
            i.update_gallery_image_url()

        for i in models.Alumni.objects.all():
            i.update_alumni_image_url()

        for i in models.Project.objects.all():
            i.update_project_cover_url()

        models.AccessModel.objects.create()
        data = {"message": "Index Updated"}
        return HttpResponse(f"{data}")

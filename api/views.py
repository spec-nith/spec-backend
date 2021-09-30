from datetime import date, datetime
from io import BytesIO
from zipfile import ZipFile

from django.core.files.images import ImageFile
from django.shortcuts import HttpResponse
from django.urls import reverse
from django.utils.timezone import make_aware
from django.views.generic import FormView, base

from api import models
from api.forms import GalleryForm, Upload


class GalleryFormView(FormView):
    template_name = "gallery.html"
    form_class = GalleryForm
    success_url = "/"

    def form_valid(self, form):
        zip_file = form.cleaned_data.pop("zip_import")
        zip_file = ZipFile(zip_file, "r")
        for name in zip_file.namelist():
            data = zip_file.read(name)
            if Upload(data).is_valid():
                form_data = form.cleaned_data
                models.Gallery.objects.create(
                    **form_data, image=ImageFile(BytesIO(data), name=name)
                )
            else:
                raise Exception("Valid Images not found")

        return super().form_valid(form)


def HomeView(request):
    return HttpResponse("<marquee><h2>I'm on</h2></marquee>")


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

        models.AccessModel.objects.create()
        data = {"message": "Index Updated"}
        return HttpResponse(f"{data}")

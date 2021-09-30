from io import BytesIO
from zipfile import ZipFile

from django.core.files.images import ImageFile
from django.shortcuts import HttpResponse
from django.views.generic import FormView

from api.forms import GalleryForm, Upload
from api.models import Gallery


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
                Gallery.objects.create(
                    **form_data, image=ImageFile(BytesIO(data), name=name)
                )
            else:
                raise Exception("Valid Images not found")

        return super().form_valid(form)


def HomeView(request):
    return HttpResponse("<marquee><h2>I'm on</h2></marquee>")

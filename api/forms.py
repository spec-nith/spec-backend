from django import forms


class GalleryForm(forms.Form):
    zip_import = forms.FileField(label="zip_import")
    event = forms.CharField(max_length=100, label="event")
    sub_event = forms.CharField(max_length=100, label="sub_event", required=False)
    date = forms.DateField()

    def __str__(self):
        return self.event


class Upload(forms.Form):
    uploaded_image = forms.ImageField()

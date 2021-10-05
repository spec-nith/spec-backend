from django import forms


class GalleryForm(forms.Form):
    event = forms.CharField(max_length=100, label="Event")
    sub_event = forms.CharField(max_length=100, label="Sub Event", required=False)
    year = forms.IntegerField(label = "Year")
    zip_import = forms.FileField(label="Zip File")

    def __str__(self):
        return self.event


class Upload(forms.Form):
    uploaded_image = forms.ImageField()

from django import forms

from api.models import Gallery


class GalleryForm(forms.ModelForm):
    sub_event = forms.CharField(max_length=100, label="Sub Event", required=False)
    year = forms.IntegerField(label="Year", required=True)
    image = forms.ImageField(
        label="Image Files", widget=forms.ClearableFileInput(attrs={"multiple": True})
    )

    class Meta:
        model = Gallery
        fields = ("event", "sub_event", "year", "image")

    def __str__(self):
        return self.event

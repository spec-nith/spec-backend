from django import forms

from api.models import Gallery, Workshop


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

class WorkshopForm(forms.ModelForm):
    description = forms.Textarea()
    event_date = forms.DateTimeField(label="Date", widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    venue = forms.CharField(max_length=100, label="Venue", required=True)
    cover = forms.ImageField(label="Cover")

    class Meta:
        model = Workshop
        fields = ("title", "description", "venue", "event_date","cover")

    def _str_(self):
        return self.title  

     

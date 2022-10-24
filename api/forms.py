from datetime import date

from django import forms
from django.forms import widgets

from api.models import BRANCH
from api.models import CHOICES
from api.models import DEGREE
from api.models import GENDER_OPTIONS
from api.models import Alumni
from api.models import Attendees
from api.models import Gallery
from api.models import MemberRegistration
from api.models import Project
from api.models import TeamModel
from api.models import Workshop


class GalleryForm(forms.ModelForm):
    event = forms.CharField(
        max_length=100,
        widget=widgets.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Event",
            }
        ),
    )

    sub_event = forms.CharField(
        max_length=100,
        label="Sub Event",
        required=True,
        widget=widgets.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Sub Event",
            }
        ),
    )
    year = forms.IntegerField(
        label="Year",
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "w-32 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Year",
            }
        ),
    )

    image = forms.ImageField(
        label="Image Files", widget=forms.ClearableFileInput(attrs={"multiple": True})
    )

    class Meta:
        model = Gallery
        fields = ("event", "sub_event", "year", "image")

    def __str__(self):
        return self.event

    def clean(self):
        super(GalleryForm, self).clean()
        year = self.cleaned_data.get("year")
        if year < 1:
            self._errors["batch"] = self.error_class(["Years cannot be negative"])

        if year > date.today().year:
            self._errors["batch"] = self.error_class(
                ["Years cannot be greater than current year"]
            )

        return self.cleaned_data


class WorkshopForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Title",
            }
        ),
    )
    description = forms.CharField(
        widget=widgets.Textarea(
            attrs={
                "class": "w-full pl-2 outline-none border-2 border-gray-400 bg-transparent rounded-xl",
                "placeholder": "Description",
            }
        ),
    )
    event_date = forms.DateTimeField(
        label="Date",
        widget=forms.widgets.DateInput(
            attrs={
                "type": "date",
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
            }
        ),
    )
    venue = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Venue",
            }
        ),
    )
    cover = forms.ImageField(label="Cover")

    class Meta:
        model = Workshop
        fields = ("title", "description", "venue", "event_date", "cover")

    def _str_(self):
        return self.title


class ProjectForm(forms.ModelForm):
    domain = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Domain",
            }
        ),
    )
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Project Name",
            }
        ),
    )
    description = forms.CharField(
        widget=widgets.Textarea(
            attrs={
                "class": "w-full pl-2 outline-none border-2 border-gray-400 bg-transparent rounded-xl",
                "placeholder": "Description",
            }
        ),
    )
    cover = forms.ImageField(label="Cover")
    year = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Year",
            }
        ),
    )
    github_link = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Github Link",
            }
        ),
    )

    class Meta:
        model = Project
        fields = ("domain", "name", "year", "description", "github_link", "cover")

    def clean(self):
        super(ProjectForm, self).clean()
        year = self.cleaned_data.get("year")
        if year < 1:
            self._errors["batch"] = self.error_class(["Years cannot be negative"])

        if year > date.today().year:
            self._errors["batch"] = self.error_class(
                ["Years cannot be greater than current year"]
            )

        return self.cleaned_data


class TeamForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Name",
            }
        )
    )
    title = forms.CharField(
        widget=forms.Select(
            choices=CHOICES,
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Designation",
            },
        )
    )

    github_id = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Github ID",
            }
        ),
    )

    linkedin_id = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Linkedin ID",
            }
        ),
    )

    profile_pic = forms.ImageField(label="Profile Pic")

    class Meta:
        model = TeamModel
        fields = ["name", "title", "github_id", "linkedin_id", "profile_pic"]


class AlumniForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Name",
            }
        )
    )
    batch = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Batch",
            }
        )
    )
    company = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Company",
            }
        )
    )

    github_id = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Github ID",
            }
        ),
    )

    linkedin_id = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Linkedin ID",
            }
        ),
    )

    profile_pic = forms.ImageField(label="Profile Pic")

    class Meta:
        model = Alumni
        fields = [
            "name",
            "batch",
            "company",
            "dual_degree",
            "github_id",
            "linkedin_id",
            "profile_pic",
        ]

    def clean(self):
        super(AlumniForm, self).clean()

        batch = self.cleaned_data.get("batch")

        if batch < 1:
            self._errors["batch"] = self.error_class(["Years cannot be negative"])

        if batch > date.today().year:
            self._errors["batch"] = self.error_class(
                ["Years cannot be greater than current year"]
            )

        return self.cleaned_data


class MemberRegistrationForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Name",
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Email",
            }
        )
    )

    gender = forms.CharField(
        widget=forms.Select(
            choices=GENDER_OPTIONS,
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Gender",
            },
        )
    )

    roll_no = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Roll Number",
            }
        )
    )

    degree = forms.CharField(
        widget=forms.Select(
            choices=DEGREE,
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Degree",
            },
        )
    )

    branch = forms.CharField(
        widget=forms.Select(
            choices=BRANCH,
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Branch",
            },
        )
    )

    year = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Current Year",
            }
        )
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Phone Number",
            }
        )
    )

    home_state = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Home State",
            }
        )
    )

    skills = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Skills",
            }
        )
    )

    strength = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Strengths",
            }
        )
    )

    weakness = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Weaknesses",
            }
        )
    )

    achievement = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Achievements",
            }
        )
    )

    application_response = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Why do you want to join SPEC?",
            }
        )
    )

    supporting_docs_link = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Supporting documents' link (Resume, Certifications, etc.)",
            }
        ),
    )

    photograph_link = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Photograph link",
            }
        ),
    )

    sign_link = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Signature link",
            }
        ),
    )

    acknowledgement = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "I agree and understand the procedures of the team interviews and a thorough line of questioning. I will hold no one accountable except for myself if I fail to adhere to the rules and regulations or fail to maintain discipline during the course of the interview. I will not hold the team and any of its members accountable for any untoward happening if selected.",
            }
        ),
    )

    class Meta:
        model = MemberRegistration
        fields = [
            "name",
            "email",
            "gender",
            "roll_no",
            "degree",
            "branch",
            "year",
            "phone",
            "home_state",
            "skills",
            "strength",
            "weakness",
            "achievement",
            "application_response",
            "supporting_docs_link",
            "photograph_link",
            "sign_link",
            "acknowledgement",
        ]


class WorkshopRegistrationForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Name",
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Email",
            }
        ),
    )

    workshop = forms.ModelChoiceField(
        queryset=Workshop.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "w-72 pl-2 outline-none border-none bg-transparent",
                "placeholder": "Workshop",
            }
        ),
    )

    class Meta:
        model = Attendees
        fields = ["name", "email"]

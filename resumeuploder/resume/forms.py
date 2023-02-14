from django import forms
from . models import resume

gender_choice=(
    ("male","male"),("female","female")
)
loc_choice=(
    ("Delhi","Delhi"),("Mumbai","Mumbai"),("Pune","Pune"),("Banglore","Banglore"),("Gurugram","Gurugram"),
)

class myform(forms.ModelForm):
    gender=forms.ChoiceField(choices=gender_choice,widget=forms.RadioSelect())
    loc=forms.MultipleChoiceField(choices=loc_choice,label="Prefered job location",widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=resume
        fields=["name","dob","gender","email","address","city","pin","state","mob","loc","img","res"]
        labels={
            "name":"Full Name","dob":"Date Of Birth","email":"Email","address":"Address","pin":"Zip Code","mob":"Contact Details","loc":"Location","res":"Resume","img":"Profile pic"
        }
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "dob":forms.DateInput(attrs={"class":"form-control","id":"datepicker"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "city":forms.TextInput(attrs={"class":"form-control"}),
            "pin":forms.NumberInput(attrs={"class":"form-control"}),
            "state":forms.Select(attrs={"class":"form-control"}),
            "mob":forms.NumberInput(attrs={"class":"form-control"}),

        }
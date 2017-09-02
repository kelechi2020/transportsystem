from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.views import login

from .models import Customer, TYPE_CHOICES


class Form_createuser(forms.ModelForm):
    # this line creates the form with four fields.it is an object which inherits from forms.Form.it contains attributes
    # that define he form fields

    name = forms.CharField(label="Name", max_length=30, required=True)
    email = forms.EmailField(label="E-mail", required=True)
    phone = forms.CharField(label="Phone Number", required=True)
    address = forms.CharField(label="Address", required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    password_bis = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    blood_group = forms.ChoiceField(label="Select Blood Group", choices=TYPE_CHOICES)
    def clean(self):
        cleaned_data = super(Form_createuser, self).clean()

        password = self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')

        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are not identical")
        return self.cleaned_data

    class Meta:
        model = Customer
        fields = ['name','email','address','password','password_bis','blood_group']

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False  # don't render form DOM element
        helper.render_unmentioned_fields = True  # render all fields
        helper.label_class = 'col-md-2'
        helper.field_class = 'col-md-10'
        return helper


class Form_login(forms.Form):
    email = forms.CharField(label="E-mail", required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False  # don't render form DOM element
        helper.render_unmentioned_fields = True  # render all fields
        helper.label_class = 'col-md-2'
        helper.field_class = 'col-md-10'
        return helper

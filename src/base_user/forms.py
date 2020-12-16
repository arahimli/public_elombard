import os
# from nocaptcha_recaptcha.fields import NoReCaptchaField
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.contrib.auth import authenticate
User = get_user_model()
from PIL import Image
GUser = get_user_model()

from home.models import *

GENDER_CHOICE = (
    (1,"Male"),
    (2,"Female"),
    (3,"Other"),
)

class LoginForm(forms.Form):
    lemail = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'autocomplete':'off','class': 'form-control login-frm-input','placeholder': _('Email'),}))
    lpassword = forms.CharField(max_length=255,required=True,widget=forms.PasswordInput(attrs={'autocomplete':'off','class': 'form-control login-frm-input','placeholder': _('Password'),}))
    # captcha = NoReCaptchaField()
    remember_me = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'autocomplete':'off','class': '',}))


class MyUserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput,
                                help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(MyUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class MyUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label=_("Password"),
                                         help_text=_(
                                             "Raw şifrələr bazada saxlanmır, onları heç cürə görmək mümkün deyil "
                                             "bu istifadəçinin şifrəsidir, lakin siz onu dəyişə bilərsiziniz "
                                             " <a href=\"../password/\">bu form</a>. vasitəsilə"))

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MyUserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


"""
    ################################################################################################
    Base System For Client Login -----------------------------------------------------------------------
    ################################################################################################
"""


class BaseAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label="İstifadəçi adı")
    password = forms.CharField(label="Parol", widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(BaseAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.EmailInput(attrs={
            'placeholder': _("E-poçt"), 'class': 'form-control form-project', 'id': 'user_email', 'autofocus': None})
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'placeholder': _("Şifrə"), 'class': 'form-control form-project', 'id': 'user_password'})

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Təəsüflər olsunki email və ya şifrə yanlışdır")
        return user


class UserRegistrationForm(forms.Form):
    name = forms.CharField(required=True,max_length=254, label="First name", error_messages={})
    surname = forms.CharField(required=True,max_length=254, label="Last name", error_messages={})
    username = forms.CharField(required=True,max_length=254, label="Username", error_messages={})
    email = forms.EmailField(required=True,error_messages={})
    phone = forms.CharField(required=True,error_messages={})
    password = forms.CharField(required=True,label=_("Password"))
    retype_password = forms.CharField(required=True,label=_("Password confirm"))
    agree = forms.BooleanField(required=True,label=_("Password confirm"))

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={
            'placeholder': _("First name"),'class':'form-control'})
        self.fields['surname'].widget = forms.TextInput(attrs={
            'placeholder': _("Last name"),'class':'form-control'})
        self.fields['username'].widget = forms.TextInput(attrs={
            'placeholder': _("Username"),'class':'form-control'})
        self.fields['email'].widget = forms.EmailInput(attrs={
            'placeholder': _("Email"),'class':'form-control'})
        self.fields['phone'].widget = forms.TextInput(attrs={
            'placeholder': _("Phone"),'class':'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'placeholder': _("Password"),'class':'form-control'})
        self.fields['retype_password'].widget = forms.PasswordInput(attrs={
            'placeholder': _("Password confirm"),'class':'form-control'})
        self.fields['agree'].widget = forms.CheckboxInput(attrs={
            })

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()

        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('retype_password')
        user_email_obj = GUser.objects.filter(email=email)
        user_username_obj = GUser.objects.filter(username=username)
        if user_email_obj:
            self._errors['email'] = _('Email is allready use')
        if user_username_obj:
            self._errors['username'] = _('Username is allready use')
        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError(_("Passwords not same"))
        return cleaned_data


    # def save(self, commit=True):
    #     name = self.cleaned_data.get('name')
    #     surname = self.cleaned_data.get('surname')
    #     username = self.cleaned_data.get('email')
    #     email = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get('password')
    #     if commit:
    #         user = User.objects.create_user(
    #             first_name=name,
    #             last_name=surname,
    #             email=email,
    #             username=username,
    #             password=password,
    #         )
    #         user.is_active = False
    #         user.save()
    #         return user
    #     else:
    #         return forms.ValidationError(_("Password beraber deyil"))

CHOSE = (
    (1, "Kişi"),
    (2, "Qadın")
)




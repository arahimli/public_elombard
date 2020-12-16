import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _
from multiupload.fields import MultiImageField

from panel.models import *

GUser = get_user_model()




class AnnuitetCalculatedForm(forms.Form):
    month_count = forms.IntegerField(required=True,label='Ay sayı', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': _('Ay sayı'),}))
    amount = forms.DecimalField(max_digits=19,decimal_places=1,label=_('Minimum Məbləğ'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Minimum Məbləğ'), 'autocomplete': 'off','class': 'form-control', }))
    percent = forms.DecimalField(max_digits=10,decimal_places=1,label=_('Maksimum Məbləğ'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Maksimum Məbləğ'), 'autocomplete': 'off','class': 'form-control', }))
    a_first_date = forms.CharField(max_length=255,label=_('İlk tarixi'), min_length=2, required=True, widget=forms.DateInput(
        attrs={'placeholder': _('İlk tarixi'), 'autocomplete': 'off',
               'class': 'form-control','data-inputmask-alias':"dd.mm.yyyy"  }))


class CustomerModelForm(forms.ModelForm):

    birthdate = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,widget=forms.DateInput(
        attrs={'placeholder': _('Doğum tarixi'), 'autocomplete': 'off',
               'class': 'form-control', }))
    class Meta:
        model = Customer
        fields = ('department', 'full_name', 'gender', 'serial_number', 'fin', 'address', 'contact_number', 'birthdate', 'profile_picture', 'passport_picture1', 'passport_picture2',)
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control', }),
            'gender': forms.Select(attrs={'class': 'form-control', }),
            'full_name': forms.TextInput(attrs={'class': 'form-control', }),
            'serial_number': forms.TextInput(attrs={'class': 'form-control', }),
            'fin': forms.TextInput(attrs={'class': 'form-control', }),
            'address': forms.TextInput(attrs={'class': 'form-control', }),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', }),
        #     'birthdate': forms.DateInput(
        # attrs={'placeholder': _('Doğum tarixi'), 'autocomplete': 'off',
        #        'class': 'form-control', }),
        }



class CustomerForm(forms.Form):
    department = forms.ChoiceField(label=_('Department'),  required=True, widget=forms.Select(
        attrs={'placeholder': _('department'), 'autocomplete': 'off',
               'class': 'form-control', }),choices=[])
    full_name = forms.CharField(max_length=255,label=_('Soyad və Ad'), min_length=2, required=True, widget=forms.TextInput(
        attrs={'placeholder': _('Soyad və Ad'), 'autocomplete': 'off',
               'class': 'form-control', }))

    gender = forms.ChoiceField(choices=GenderChoice,label=_('Cins'),  required=True, widget=forms.Select(attrs={'placeholder': _('Cins'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    serial_number = forms.CharField(max_length=255,label=_('Seriya nömrəsi'), min_length=2, required=True, widget=forms.TextInput(
        attrs={'placeholder': _('Seriya nömrəsi'), 'autocomplete': 'off',
               'class': 'form-control', }))
    fin = forms.CharField(max_length=255,label=_('Fin kod'), min_length=2, required=True, widget=forms.TextInput(
        attrs={'placeholder': _('Fin kod'), 'autocomplete': 'off',
               'class': 'form-control', }))
    address = forms.CharField(max_length=255,label=_('Adres'), min_length=2, required=True, widget=forms.TextInput(
        attrs={'placeholder': _('Adres'), 'autocomplete': 'off',
               'class': 'form-control', }))
    contact_number = forms.CharField(max_length=255,label=_('Kontakt nömrəsi'), min_length=2, required=True, widget=forms.TextInput(
        attrs={'placeholder': _('(050) 999-99-99'), 'autocomplete': 'off',
               'class': 'form-control', }))
    birthdate = forms.CharField(max_length=255,label=_('Doğum tarixi'), min_length=2, required=True, widget=forms.TextInput(
        attrs={'placeholder': _('Doğum tarixi'), 'autocomplete': 'off',
               'class': 'form-control', }))
    profile_picture = forms.ImageField(required=False,label='Profil şəkli seç')
    passport_picture1 = forms.ImageField(required=False,label='Passport uz şəkli seç')
    passport_picture2 = forms.ImageField(required=False,label='Passport arxa şəkli seç')
    is_active = forms.BooleanField(required=False,label=_('Status'))
    # id = 0

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

        self.fields['department'].choices = [[x.id, x.title] for x in Department.objects.filter()]


    def clean(self):
        cleaned_data = self.cleaned_data
        profile_picture = cleaned_data.get('profile_picture')
        if id:
            pass
        else:
            if profile_picture:
                pass
            else:
                raise forms.ValidationError(_('Image is required'))

class CustomerSearchForm(forms.Form):
    s_full_name = forms.CharField(max_length=255,label=_('Soyad, Ad, Ata adı '), required=False, widget=forms.TextInput(
        attrs={'placeholder': _('Soyad, Ad, Ata adı '), 'autocomplete': 'off',
               'class': 'form-control', }))
    s_serial_number = forms.CharField(max_length=255,label=_('Seriya nömrəsi'),required=False, widget=forms.TextInput(
        attrs={'placeholder': _('Seriya nömrəsi'), 'autocomplete': 'off',
               'class': 'form-control', }))
    s_fin = forms.CharField(max_length=255,label=_('Fin kod'), required=False, widget=forms.TextInput(
        attrs={'placeholder': _('Fin kod'), 'autocomplete': 'off',
               'class': 'form-control', }))
    s_address = forms.CharField(max_length=255,label=_('Adres'), min_length=2, required=False, widget=forms.TextInput(
        attrs={'placeholder': _('Adres'), 'autocomplete': 'off',
               'class': 'form-control', }))
    s_contact_number = forms.CharField(max_length=255,label=_('Kontakt nömrəsi'), required=False, widget=forms.TextInput(
        attrs={'placeholder': _('(050) 999-99-99'), 'autocomplete': 'off','data-mask':'(099) 999-99-99',
               'class': 'form-control', }))
    id_number = forms.CharField(max_length=255,label=_('Id number'), required=False, widget=forms.TextInput(
        attrs={'placeholder': _('Id number'), 'autocomplete': 'off',
               'class': 'form-control', }))

CustomerStatusChoice = (
    ('','Paket tipi'),
    ('no-package','Paketi olmayan'),
    ('active','Aktiv'),
    ('deactive','Deaktiv'),
    ('saled','Satılan'),
)

class CustomerMainSearchForm(forms.Form):
    full_name = forms.CharField(max_length=255,label=_('Soyad, Ad, Ata adı '), required=False, widget=forms.TextInput(
        attrs={'placeholder': _('Soyad, Ad, Ata adı '), 'autocomplete': 'off',
               'class': 'form-control', }))

    serial_number = forms.CharField(max_length=255,label=_('Seriya nömrəsi'),required=False, widget=forms.TextInput(
        attrs={'placeholder': _('Seriya nömrəsi'), 'autocomplete': 'off',
               'class': 'form-control', }))
    fin = forms.CharField(max_length=255,label=_('Fin kod'), required=False, widget=forms.TextInput(
        attrs={'placeholder': _('Fin kod'), 'autocomplete': 'off',
               'class': 'form-control', }))
    address = forms.CharField(max_length=255,label=_('Adres'), min_length=2, required=False, widget=forms.TextInput(
        attrs={'placeholder': _('Adres'), 'autocomplete': 'off',
               'class': 'form-control', }))
    contact_number = forms.CharField(max_length=255,label=_('Kontakt nömrəsi'), required=False, widget=forms.TextInput(
        attrs={'placeholder': _('(050) 999-99-99'), 'autocomplete': 'off','data-mask':'(099) 999-99-99',
               'class': 'form-control', }))
    id_number = forms.CharField(max_length=255,label=_('Id number'), required=False, widget=forms.TextInput(
        attrs={'placeholder': _('Id number'), 'autocomplete': 'off',
               'class': 'form-control', }))
    status = forms.ChoiceField(choices=CustomerStatusChoice,label=_('Status'),  required=False, widget=forms.Select(attrs={'placeholder': _('Status'), 'autocomplete': 'off','class': 'form-control', }))

    gender = forms.ChoiceField(choices=GenderChoice,label=_('Status'),  required=False, widget=forms.Select(attrs={'placeholder': _('Status'), 'autocomplete': 'off','class': 'form-control', }))
    show_photo = forms.ChoiceField(choices=ShowPhotoChoice, label=_('Status'), required=False, widget=forms.Select(
        attrs={'placeholder': _('Status'), 'autocomplete': 'off', 'class': 'form-control', }))


# class PackageSearchForm(forms.Form):
#     s_full_name = forms.CharField(max_length=255,label=_('Soyad, Ad, Ata adı '), required=False, widget=forms.TextInput(
#         attrs={'placeholder': _('Soyad, Ad, Ata adı '), 'autocomplete': 'off',
#                'class': 'form-control', }))
#     s_serial_number = forms.CharField(max_length=255,label=_('Seriya nömrəsi'),required=False, widget=forms.TextInput(
#         attrs={'placeholder': _('Seriya nömrəsi'), 'autocomplete': 'off',
#                'class': 'form-control', }))
#     s_fin = forms.CharField(max_length=255,label=_('Fin kod'), required=False, widget=forms.TextInput(
#         attrs={'placeholder': _('Fin kod'), 'autocomplete': 'off',
#                'class': 'form-control', }))
#     s_address = forms.CharField(max_length=255,label=_('Adres'), min_length=2, required=False, widget=forms.TextInput(
#         attrs={'placeholder': _('Adres'), 'autocomplete': 'off',
#                'class': 'form-control', }))
#     s_contact_number = forms.CharField(max_length=255,label=_('Kontakt nömrəsi'), required=False, widget=forms.TextInput(
#         attrs={'placeholder': _('(050) 999-99-99'), 'autocomplete': 'off','data-mask':'(099) 999-99-99',
#                'class': 'form-control', }))
#


MonthChoice = (
    (1,'Yanvar'),
    (2,'Fevral'),
    (3,'Mart'),
    (4,'Aprel'),
    (5,'May'),
    (6,'Iyun'),
    (7,'Iyul'),
    (8,'Avqust'),
    (9,'Sentyabr'),
    (10,'Oktyabr'),
    (11,'Noyabr'),
    (12,'Dekabr'),
)


class StatisticDailyForm(forms.Form):
    month = forms.ChoiceField(required=False, choices=MonthChoice, widget=forms.Select(attrs={'placeholder': _('Ay'), 'autocomplete': 'off','class': 'form-control', }))
    year = forms.ChoiceField(required=False, widget=forms.Select(attrs={'placeholder': _('İl'), 'autocomplete': 'off','class': 'form-control', }))
    def __init__(self, *args, **kwargs):
        super(StatisticDailyForm, self).__init__(*args, **kwargs)

        self.fields['year'].choices = [[x, x] for x in range(2000,datetime.datetime.now().year + 1)]



class SalaryForm(forms.Form):
    month = forms.ChoiceField(required=False, choices=MonthChoice, widget=forms.Select(attrs={'placeholder': _('Ay'), 'autocomplete': 'off','class': 'form-control', }))
    year = forms.ChoiceField(required=False, widget=forms.Select(attrs={'placeholder': _('İl'), 'autocomplete': 'off','class': 'form-control', }))
    month_day_count = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'Gün sayı', 'autocomplete': 'off', 'class': 'form-control', }))
    department = forms.ChoiceField(choices=[],label=_('Department'),  required=False, widget=forms.Select(attrs={'placeholder': _('Department'), 'autocomplete': 'off','class': 'form-control', }))
    def __init__(self, *args, **kwargs):
        super(SalaryForm, self).__init__(*args, **kwargs)

        self.fields['year'].choices = [[x, x] for x in range(2015,datetime.datetime.now().year + 1)]
        self.fields['department'].choices = [[x.id, x.title] for x in Department.objects.filter(removed=False)]



from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField


class PackageForm(forms.Form):
    customer_name = forms.CharField(label=_('Müştəri'), required=True, widget=forms.TextInput(attrs={'placeholder': _('Müştəri'),'readonly': True, 'autocomplete': 'off','class': 'form-control', }))
    customer_id = forms.IntegerField(required=True, widget=forms.HiddenInput(attrs={'readonly': True, }))
    pledge_number = forms.CharField(max_length=255,label=_('Girov nömrəsi'), min_length=2, required=True, widget=forms.TextInput(attrs={'placeholder': _('Girov nömrəsi'), 'autocomplete': 'off','class': 'form-control', }))
    currency = forms.ChoiceField(choices=[],label=_('Valyuta'),  required=True, widget=forms.Select(attrs={'placeholder': _('Fin kod'), 'autocomplete': 'off','class': 'form-control', }))

    first_date = forms.CharField(max_length=255,label=_('Başlanğıc tarixi'), min_length=2, required=False, widget=forms.TextInput(attrs={'placeholder': _('Başlanğıc tarixi'), 'autocomplete': 'off','class': 'form-control','readonly': True, }))
    # end_date = forms.CharField(max_length=255,label=_('Bitiş tarixi'), min_length=2, required=True, widget=forms.DateInput(attrs={'placeholder': _('Bitiş tarixi'), 'autocomplete': 'off','class': 'form-control', }))
    percent = forms.DecimalField(max_digits=10,decimal_places=2,label=_('Faiz'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Faiz'), 'autocomplete': 'off','class': 'form-control', }))
    notes = forms.CharField(label=_('Qeydlər'), required=False, widget=forms.Textarea(attrs={'placeholder': _('Qeydlər'), 'autocomplete': 'off','class': 'form-control','rows':3 }))

    amount = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Məbləğ'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Məbləğ'), 'autocomplete': 'off','class': 'form-control', }))
    # debt_amount = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Qalan məbləğ'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Borc məbləği'), 'autocomplete': 'off','class': 'form-control', }))
    # amount_dollar = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Məbləğ dollar ilə'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Məbləğ dollar ilə'), 'autocomplete': 'off','class': 'form-control', }))
    # status = forms.CharField(label=_('Status'),  required=True, widget=forms.TextInput(attrs={'placeholder': _('Status'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    status = forms.ChoiceField(choices=PackageStatusFormChoice,label=_('Status'),  required=False, widget=forms.Select(attrs={'placeholder': _('Status'), 'autocomplete': 'off','class': 'form-control', 'disabled':True}))

    packet_type = forms.ChoiceField(choices=[],label=_('Paket növü'), required=True, widget=forms.Select(attrs={'placeholder': _('Paket növü'), 'autocomplete': 'off','class': 'form-control', }))
    department = forms.ChoiceField(choices=[],label=_('Department'), required=False, widget=forms.Select(attrs={'placeholder': _('Department'), 'autocomplete': 'off','class': 'form-control', }))


    # product = forms.ChoiceField(choices=[],label=_('Girov'), required=True, widget=forms.Select(attrs={'placeholder': _('Girov'), 'autocomplete': 'off','class': 'form-control', }))
    # product_type = forms.ChoiceField(choices=[],label=_('Girov növü'), required=False, widget=forms.Select(attrs={'placeholder': _('Girov növü'), 'autocomplete': 'off','class': 'form-control', }))
    # product_amount = forms.DecimalField(max_digits=10,decimal_places=2,label=_('Miqdar'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Miqdar'), 'autocomplete': 'off','class': 'form-control', }))


    annuitet = forms.BooleanField(required=False,label=_('Annuitet'),widget=forms.CheckboxInput(attrs={'class': 'form-control', }))
    pay_date = forms.CharField(max_length=255,label=_('Ödəniş tarixi'), required=False, widget=forms.DateInput(attrs={'placeholder': _('Ödəniş tarixi'), 'autocomplete': 'off','class': 'form-control', }))
    # money_rate = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Money rate'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Money rate'), 'autocomplete': 'off','class': 'form-control', }))

    def __init__(self, *args, **kwargs):
        super(PackageForm, self).__init__(*args, **kwargs)

        self.fields['currency'].choices = [[x.id, x.title] for x in Currency.objects.filter(removed=False)]
        # self.fields['status'].choices = [[x.id, x.title] for x in PackageStatus.objects.filter()]
        self.fields['packet_type'].choices = [[x.id, x.title] for x in PackageType.objects.filter(removed=False)]
        self.fields['department'].choices = [[x.id, x.title] for x in Department.objects.filter(removed=False)]
        # self.fields['product'].choices = [[x.id, x.title] for x in Product.objects.filter(removed=False)]
        # self.fields['product_type'].choices = [[x.id, x.title] for x in ProductType.objects.filter(removed=False)]

# class PackageProductTypeForm(forms.ModelForm):
#     class Meta:
#         model = PackageProduct
#         exclude = ()

class AttachmentForm(forms.Form):
    attachments = MultiImageField(min_num=0, max_num=20, max_file_size=1024 * 1024 * 20, label='Girov şəkli')


class PackageProductTypeForm(forms.Form):
    product_type = forms.ChoiceField(choices=[],label=_('Girov növü'), required=True, widget=forms.Select(attrs={'placeholder': _('Girov növü'), 'autocomplete': 'off','class': 'form-control', }))
    product_amount = forms.DecimalField(max_digits=10,decimal_places=2,label=_('Miqdar'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Miqdar'), 'autocomplete': 'off','class': 'form-control', }))

    def __init__(self, *args, **kwargs):
        super(PackageProductTypeForm, self).__init__(*args, **kwargs)

        self.fields['product_type'].choices = [[x.id, x.title] for x in ProductType.objects.filter()]

class PackageSearchForm(forms.Form):
    customer_name = forms.CharField(label=_('Soyad, Ad, Ata adı '), required=False, widget=forms.TextInput(attrs={'placeholder': _('Soyad, Ad, Ata adı '), 'autocomplete': 'off','class': 'form-control', }))
    s_serial_number = forms.CharField(max_length=255,label=_('Seriya nömrəsi'),required=False, widget=forms.TextInput(attrs={'placeholder': _('Seriya nömrəsi'), 'autocomplete': 'off','class': 'form-control', }))
    s_fin = forms.CharField(max_length=255,label=_('Fin kod'), required=False, widget=forms.TextInput(attrs={'placeholder': _('Fin kod'), 'autocomplete': 'off','class': 'form-control', }))

    package_id = forms.CharField(required=False,label='Paket N', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Paket N'),}))
    currency = forms.ChoiceField(choices=[],label=_('Valyuta'),  required=False, widget=forms.Select(attrs={'placeholder': _('Fin kod'), 'autocomplete': 'off','class': 'form-control', }))
    start_date = forms.CharField(max_length=255,label=_('Başlanğıc tarix'), min_length=2, required=False, widget=forms.TextInput(attrs={'placeholder': _('Başlanğıc tarix'), 'autocomplete': 'off','class': 'form-control'}))
    end_date = forms.CharField(max_length=255,label=_('Son tarix'), min_length=2, required=False, widget=forms.TextInput(attrs={'placeholder': _('Son tarix'), 'autocomplete': 'off','class': 'form-control', }))
    # end_date = forms.CharField(max_length=255,label=_('Bitiş tarixi'), min_length=2, required=False, widget=forms.DateInput(attrs={'placeholder': _('Bitiş tarixi'), 'autocomplete': 'off','class': 'form-control', }))
    percent = forms.DecimalField(max_digits=10,decimal_places=2,label=_('Faiz'), required=False, widget=forms.NumberInput(attrs={'placeholder': _('Faiz'), 'autocomplete': 'off','class': 'form-control', }))

    amount_min = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Minimum Məbləğ'), required=False, widget=forms.NumberInput(attrs={'placeholder': _('Minimum Məbləğ'), 'autocomplete': 'off','class': 'form-control', }))
    amount_max = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Maksimum Məbləğ'), required=False, widget=forms.NumberInput(attrs={'placeholder': _('Maksimum Məbləğ'), 'autocomplete': 'off','class': 'form-control', }))
    status = forms.ChoiceField(choices=PackageStatusFormChoice,label=_('Status'),  required=False, widget=forms.Select(attrs={'placeholder': _('Status'), 'autocomplete': 'off','class': 'form-control', }))
    annuitet = forms.ChoiceField(choices=AnnuitetStatusChoice,label=_('Annuitet'),  required=False, widget=forms.Select(attrs={'placeholder': _('Annuitet'), 'autocomplete': 'off','class': 'form-control', }))

    packet_type = forms.ChoiceField(choices=[],label=_('Paket növü'), required=False, widget=forms.Select(attrs={'placeholder': _('Paket növü'), 'autocomplete': 'off','class': 'form-control', }))
    department = forms.ChoiceField(choices=[],label=_('Department'), required=False, widget=forms.Select(attrs={'placeholder': _('Department'), 'autocomplete': 'off','class': 'form-control', }))
    # money_rate = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Money rate'), required=False, widget=forms.NumberInput(attrs={'placeholder': _('Money rate'), 'autocomplete': 'off','class': 'form-control', }))
    # commission_fee = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Komisiya haqqı'), required=False, widget=forms.NumberInput(attrs={'placeholder': _('Komisiya haqqı'), 'autocomplete': 'off','class': 'form-control', }))

    def __init__(self, *args, **kwargs):
        super(PackageSearchForm, self).__init__(*args, **kwargs)

        self.fields['currency'].choices = [['', 'Valyuta']] + [[x.id, x.title] for x in Currency.objects.filter()]
        self.fields['department'].choices = [['', 'Filial']] + [[x.id, x.title] for x in Department.objects.filter()]
        self.fields['packet_type'].choices = [['', 'Paket tipi']] + [[x.id, x.title] for x in PackageType.objects.filter()]


class PackageNoteSearchForm(forms.Form):

    package_id = forms.IntegerField(required=False,label='Paket N', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': _('Paket N'),}))
    currency = forms.ChoiceField(choices=[],label=_('Valyuta'),  required=False, widget=forms.Select(attrs={'placeholder': _('Fin kod'), 'autocomplete': 'off','class': 'form-control', }))
    start_date = forms.CharField(max_length=255,label=_('Başlanğıc tarix'), min_length=2, required=False, widget=forms.TextInput(attrs={'placeholder': _('Başlanğıc tarix'), 'autocomplete': 'off','class': 'form-control'}))
    end_date = forms.CharField(max_length=255,label=_('Son tarix'), min_length=2, required=False, widget=forms.TextInput(attrs={'placeholder': _('Son tarix'), 'autocomplete': 'off','class': 'form-control', }))

    amount_min = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Minimum Məbləğ'), required=False, widget=forms.NumberInput(attrs={'placeholder': _('Minimum Məbləğ'), 'autocomplete': 'off','class': 'form-control', }))
    amount_max = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Maksimum Məbləğ'), required=False, widget=forms.NumberInput(attrs={'placeholder': _('Maksimum Məbləğ'), 'autocomplete': 'off','class': 'form-control', }))
    status = forms.ChoiceField(choices=PackageStatusChoice,label=_('Status'),  required=False, widget=forms.Select(attrs={'placeholder': _('Status'), 'autocomplete': 'off','class': 'form-control', }))

    department = forms.ChoiceField(choices=[],label=_('Department'), required=False, widget=forms.Select(attrs={'placeholder': _('Department'), 'autocomplete': 'off','class': 'form-control', }))
    # money_rate = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Money rate'), required=False, widget=forms.NumberInput(attrs={'placeholder': _('Money rate'), 'autocomplete': 'off','class': 'form-control', }))
    # commission_fee = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Komisiya haqqı'), required=False, widget=forms.NumberInput(attrs={'placeholder': _('Komisiya haqqı'), 'autocomplete': 'off','class': 'form-control', }))

    def __init__(self, *args, **kwargs):
        super(PackageNoteSearchForm, self).__init__(*args, **kwargs)

        self.fields['currency'].choices = [['', 'Valyuta']] + [[x.id, x.title] for x in Currency.objects.filter()]
        self.fields['department'].choices = [['', 'Filial']] + [[x.id, x.title] for x in Department.objects.filter()]





class PackageClosedReasonForm(forms.Form):
    closed_reason = forms.CharField(label=_('Bağlanma səbəbi'), min_length=2, required=False, widget=forms.Textarea(attrs={'placeholder': _('Bağlanma səbəbi'), 'autocomplete': 'off','class': 'form-control','rows':3 }))


class PackageEditForm(forms.Form):
    customer_name = forms.CharField(label=_('Müştəri'), required=True, widget=forms.TextInput(attrs={'placeholder': _('Müştəri'),'readonly': True, 'autocomplete': 'off','class': 'form-control', }))
    # customer_id = forms.IntegerField(required=True, widget=forms.HiddenInput(attrs={'readonly': True, }))
    pledge_number = forms.CharField(max_length=255,label=_('Girov nömrəsi'), min_length=2, required=True, widget=forms.TextInput(attrs={'placeholder': _('Girov nömrəsi'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    currency = forms.ChoiceField(choices=[],label=_('Valyuta'),  required=True, widget=forms.Select(attrs={'placeholder': _('Fin kod'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))

    first_date = forms.CharField(max_length=255,label=_('Başlanğıc tarixi'), min_length=2, required=False, widget=forms.TextInput(attrs={'placeholder': _('Başlanğıc tarixi'), 'autocomplete': 'off','class': 'form-control','readonly': True, }))
    # end_date = forms.CharField(max_length=255,label=_('Bitiş tarixi'), min_length=2, required=True, widget=forms.DateInput(attrs={'placeholder': _('Bitiş tarixi'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    percent = forms.DecimalField(max_digits=10,decimal_places=2,label=_('Faiz'), required=False, widget=forms.NumberInput(attrs={'placeholder': _('Faiz'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    notes = forms.CharField(label=_('Qeydlər'), min_length=2, required=False, widget=forms.Textarea(attrs={'placeholder': _('Qeydlər'), 'autocomplete': 'off','class': 'form-control','rows':3 }))

    amount = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Məbləğ'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Məbləğ'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    debt_amount = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Qalan məbləğ'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Borc məbləği'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    status = forms.ChoiceField(choices=PackageStatusChoice,label=_('Status'),  required=False, widget=forms.Select(attrs={'placeholder': _('Status'), 'autocomplete': 'off','class': 'form-control', 'disabled': True, }))

    packet_type = forms.ChoiceField(choices=[],label=_('Paket növü'), required=False, widget=forms.Select(attrs={'placeholder': _('Paket növü'), 'autocomplete': 'off','class': 'form-control', 'disabled': True, }))
    department = forms.ChoiceField(choices=[],label=_('Department'), required=False, widget=forms.Select(attrs={'placeholder': _('Department'), 'autocomplete': 'off','class': 'form-control', }))

    product = forms.ChoiceField(choices=[],label=_('Girov'), required=False, widget=forms.Select(attrs={'placeholder': _('Girov'), 'autocomplete': 'off','class': 'form-control', 'disabled': True, }))
    product_type = forms.ChoiceField(choices=[],label=_('Girov növü'), required=False, widget=forms.Select(attrs={'placeholder': _('Girov növü'), 'autocomplete': 'off','class': 'form-control', 'disabled': True, }))
    product_amount = forms.DecimalField(max_digits=10,decimal_places=2,label=_('Miqdar'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Miqdar'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))

    annuitet = forms.BooleanField(required=False,label=_('Annuitet'),widget=forms.CheckboxInput(attrs={'class': 'form-control', }))
    # attachments = MultiImageField(min_num=0, max_num=20, max_file_size=1024*1024*5,label='Girov şəkli əlavə et')
    pay_date = forms.CharField(max_length=255,label=_('Ödəniş tarixi'), required=False, widget=forms.DateInput(attrs={'placeholder': _('Ödəniş tarixi'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    # money_rate = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Money rate'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Money rate'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    # commission_fee = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Komisiya haqqı'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Komisiya haqqı'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))

    def __init__(self, *args, **kwargs):
        super(PackageEditForm, self).__init__(*args, **kwargs)

        self.fields['currency'].choices = [[x.id, x.title] for x in Currency.objects.filter()]
        # self.fields['status'].choices = [[x.id, x.title] for x in PackageStatus.objects.filter()]
        self.fields['packet_type'].choices = [[x.id, x.title] for x in PackageType.objects.filter()]
        self.fields['department'].choices = [[x.id, x.title] for x in Department.objects.filter()]
        self.fields['product'].choices = [[x.id, x.title] for x in Product.objects.filter(removed=False)]
        self.fields['product_type'].choices = [[x.id, x.title] for x in ProductType.objects.filter(removed=False)]



class PackageAdminEditForm(forms.Form):
    customer_name = forms.CharField(label=_('Müştəri'), required=True, widget=forms.TextInput(attrs={'placeholder': _('Müştəri'),'readonly': True, 'autocomplete': 'off','class': 'form-control', }))
    # customer_id = forms.IntegerField(required=True, widget=forms.HiddenInput(attrs={'readonly': True, }))
    pledge_number = forms.CharField(max_length=255,label=_('Girov nömrəsi'), min_length=2, required=True, widget=forms.TextInput(attrs={'placeholder': _('Girov nömrəsi'), 'autocomplete': 'off','class': 'form-control', 'readonly': False, }))
    currency = forms.ChoiceField(choices=[],label=_('Valyuta'),  required=True, widget=forms.Select(attrs={'placeholder': _('Fin kod'), 'autocomplete': 'off','class': 'form-control', 'readonly': False, }))

    first_date = forms.CharField(max_length=255,label=_('Başlanğıc tarixi'), min_length=2, required=False, widget=forms.TextInput(attrs={'placeholder': _('Başlanğıc tarixi'), 'autocomplete': 'off','class': 'form-control','readonly': False, }))
    # end_date = forms.CharField(max_length=255,label=_('Bitiş tarixi'), min_length=2, required=True, widget=forms.DateInput(attrs={'placeholder': _('Bitiş tarixi'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    percent = forms.DecimalField(max_digits=10,decimal_places=2,label=_('Faiz'), required=False, widget=forms.NumberInput(attrs={'placeholder': _('Faiz'), 'autocomplete': 'off','class': 'form-control', 'readonly': False, }))
    notes = forms.CharField(label=_('Qeydlər'), min_length=2, required=False, widget=forms.Textarea(attrs={'placeholder': _('Qeydlər'), 'autocomplete': 'off','class': 'form-control','rows':3 }))

    amount = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Məbləğ'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Məbləğ'), 'autocomplete': 'off','class': 'form-control', 'readonly': False, }))
    debt_amount = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Qalan məbləğ'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Borc məbləği'), 'autocomplete': 'off','class': 'form-control', 'readonly': False, }))
    status = forms.ChoiceField(choices=PackageStatusChoice,label=_('Status'),  required=False, widget=forms.Select(attrs={'placeholder': _('Status'), 'autocomplete': 'off','class': 'form-control', 'disabled': True, }))

    packet_type = forms.ChoiceField(choices=[],label=_('Paket növü'), required=False, widget=forms.Select(attrs={'placeholder': _('Paket növü'), 'autocomplete': 'off','class': 'form-control', 'disabled': False, }))
    department = forms.ChoiceField(choices=[],label=_('Department'), required=False, widget=forms.Select(attrs={'placeholder': _('Department'), 'autocomplete': 'off','class': 'form-control', }))

    annuitet = forms.BooleanField(required=False,label=_('Annuitet'),widget=forms.CheckboxInput(attrs={'class': 'form-control', }))
    # attachments = MultiImageField(min_num=0, max_num=20, max_file_size=1024*1024*5,label='Girov şəkli əlavə et')
    pay_date = forms.CharField(max_length=255,label=_('Ödəniş tarixi'), required=False, widget=forms.DateInput(attrs={'placeholder': _('Ödəniş tarixi'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    # money_rate = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Money rate'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Money rate'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    # commission_fee = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Komisiya haqqı'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Komisiya haqqı'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))

    def __init__(self, *args, **kwargs):
        super(PackageAdminEditForm, self).__init__(*args, **kwargs)

        self.fields['currency'].choices = [[x.id, x.title] for x in Currency.objects.filter()]
        # self.fields['status'].choices = [[x.id, x.title] for x in PackageStatus.objects.filter()]
        self.fields['packet_type'].choices = [[x.id, x.title] for x in PackageType.objects.filter()]
        self.fields['department'].choices = [[x.id, x.title] for x in Department.objects.filter()]





class PackagePaymentPayDateForm(forms.Form):
    pd_pay_date = forms.CharField(max_length=255,label=_('Odəməli olan tarix'), required=False, widget=forms.DateInput(attrs={'placeholder': _('Odəməli olan tarix'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    pd_paid_date = forms.CharField(max_length=255,label=_('Odənilen tarix'), required=False, widget=forms.DateInput(attrs={'placeholder': _('Odənilen tarix'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    pd_pay_amount = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Odənilən miqdar'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Odənilən miqdar'), 'autocomplete': 'off','class': 'form-control', }))
    pd_amount = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Əsas miqdar'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Əsas miqdar'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    pd_debt_amount = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Qalan məbləğ'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Qalan məbləğ'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    pd_percent_amount = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Faiz miqdarı'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Faiz miqdarı'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    pd_percent = forms.DecimalField(max_digits=10,decimal_places=2,label=_('Faiz'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Faiz'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    def clean(self):
        cleaned_data = super(PackagePaymentPayDateForm, self).clean()

        percent_amount = cleaned_data.get('pd_percent_amount')
        pay_amount = cleaned_data.get('pd_pay_amount')
        if pay_amount <= 0:
            self._errors['pd_pay_amount'] = _('0 dan kiçik ola bilməz')
        print('{}    -----   {}'.format(percent_amount,pay_amount))
        if percent_amount > pay_amount:
            self._errors['pd_pay_amount'] = _('Fazi məbləğindən az pul yatırmaq olmaz')




class PackagePaymentPayForm(forms.Form):
    pd_delay_day = forms.IntegerField(label=_('Gecikmə'), required=False, widget=forms.NumberInput(attrs={'placeholder': _('Gecikmə'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    pd_paid_date = forms.CharField(max_length=255,label=_('Odənilən tarix'), required=False, widget=forms.DateInput(attrs={'placeholder': _('Odənilən tarix'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    pd_month_count = forms.IntegerField(label=_('Ay sayı'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Ay sayı'), 'autocomplete': 'off','class': 'form-control', }))
    pd_day_count = forms.IntegerField(label=_('Gün sayı'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Gün sayı'), 'autocomplete': 'off','class': 'form-control', }))
    pd_pay_amount = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Odənilən miqdar'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Odənilən miqdar'), 'autocomplete': 'off','class': 'form-control', }))
    pd_calculated_percent = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Odənilən miqdar'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Odənilən miqdar'), 'autocomplete': 'off','class': 'form-control', }))
    pd_paid_percent = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Odənilən miqdar'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Odənilən miqdar'), 'autocomplete': 'off','class': 'form-control', }))
    pd_percent_debt = forms.DecimalField(max_digits=19,decimal_places=2,label=_('Odənilən miqdar'), required=True, widget=forms.NumberInput(attrs={'placeholder': _('Odənilən miqdar'), 'autocomplete': 'off','class': 'form-control', }))
    pd_description = forms.CharField(max_length=255,label=_('Qeyd'), required=False, widget=forms.TextInput(attrs={'placeholder': _('Qeyd'), 'autocomplete': 'off','class': 'form-control', 'readonly': True, }))
    def clean(self):
        cleaned_data = super(PackagePaymentPayForm, self).clean()
        #
        # percent_amount = cleaned_data.get('pd_percent_amount')
        # pay_amount = cleaned_data.get('pd_pay_amount')
        # if pay_amount <= 0:
        #     self._errors['pd_pay_amount'] = _('0 dan kiçik ola bilməz')
        # print('{}    -----   {}'.format(percent_amount,pay_amount))
        # if percent_amount > pay_amount:
        #     self._errors['pd_pay_amount'] = _('Fazi məbləğindən az pul yatırmaq olmaz')


class EmployeeForm(forms.Form):
    department = forms.ChoiceField(required=True, label="Department", error_messages={})
    permissions_department = forms.MultipleChoiceField(required=False, label="Icazəli Departmentlər", error_messages={})
    name = forms.CharField(required=True,max_length=254, label="Ad", error_messages={})
    surname = forms.CharField(required=True,max_length=254, label="Soyad", error_messages={})
    email = forms.EmailField(required=True,error_messages={},label=_('Email'))
    phone = forms.CharField(required=True,error_messages={},label=_('Nömrə'))
    password = forms.CharField(required=True, min_length=6,label=_("Şifrə"))
    retype_password = forms.CharField(required=True,min_length=6,label=_("Şifrə təsdiqi"))

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        departments = [[x.id, x.title] for x in Department.objects.filter()]
        self.fields['department'].widget = forms.Select(attrs={
            'placeholder': _("department"),'class':'js-basic-single form-control'})
        self.fields['department'].choices = [["", _("-- Select department --")]] + departments
        self.fields['permissions_department'].widget = forms.SelectMultiple(attrs={
            'placeholder': _("Icazəli Departmentlər"),'class':'js-basic-multiple form-control '})
        self.fields['permissions_department'].choices = departments
        self.fields['name'].widget = forms.TextInput(attrs={
            'placeholder': _("Ad"),'class':'form-control'})
        self.fields['surname'].widget = forms.TextInput(attrs={
            'placeholder': _("Soyad"),'class':'form-control'})
        self.fields['email'].widget = forms.EmailInput(attrs={
            'placeholder': _("Email"),'class':'form-control'})
        self.fields['phone'].widget = forms.TextInput(attrs={
            'placeholder': _("Nömrə"),'class':'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'placeholder': _("Şifrə"),'class':'form-control'})
        self.fields['retype_password'].widget = forms.PasswordInput(attrs={
            'placeholder': _("Şifrə təsdiqi"),'class':'form-control'})

    def clean(self):
        cleaned_data = super(EmployeeForm, self).clean()

        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('retype_password')
        user_email_obj = GUser.objects.filter(email=email)
        if user_email_obj:
            self._errors['email'] = _('Email is allready use')
        if user_email_obj:
            self._errors['username'] = _('Email is allready use')
        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError(_("Passwords not same"))
        return cleaned_data






class WaitingPackageEditForm(forms.Form):
    date = forms.CharField(max_length=255, label=_('Tarix'), min_length=2, required=True,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': _('Tarix'), 'autocomplete': 'off',
                                            'class': 'form-control'}))

class EmployeeEditForm(forms.Form):
    department = forms.ChoiceField(required=True, label="Department", error_messages={})
    permissions_department = forms.MultipleChoiceField(required=False, label="Icazəli Departmentlər", error_messages={})
    name = forms.CharField(required=True,max_length=254, label="Ad", error_messages={})
    surname = forms.CharField(required=True,max_length=254, label="Soyad", error_messages={})
    email = forms.EmailField(required=True,error_messages={},label=_('Email'))
    phone = forms.CharField(required=True,error_messages={},label=_('Nömrə'))
    password = forms.CharField(required=False,label=_("Şifrə"))
    retype_password = forms.CharField(required=False,label=_("Şifrə təsdiqi"))
    user_id = 0

    def __init__(self,user_id, *args, **kwargs):
        super(EmployeeEditForm, self).__init__(*args, **kwargs)
        self.user_id = user_id
        departments = [[x.id, x.title] for x in Department.objects.filter()]
        self.fields['department'].widget = forms.Select(attrs={
            'placeholder': _("department"),'class':'js-basic-single form-control'})
        self.fields['department'].choices = [["", _("-- Select department --")]] + departments
        self.fields['permissions_department'].widget = forms.SelectMultiple(attrs={
            'placeholder': _("Icazəli Departmentlər"),'class':'js-basic-multiple form-control '})
        self.fields['permissions_department'].choices = departments
        self.fields['name'].widget = forms.TextInput(attrs={
            'placeholder': _("Ad"),'class':'form-control'})
        self.fields['surname'].widget = forms.TextInput(attrs={
            'placeholder': _("Soyad"),'class':'form-control'})
        self.fields['email'].widget = forms.EmailInput(attrs={
            'placeholder': _("Email"),'class':'form-control'})
        self.fields['phone'].widget = forms.TextInput(attrs={
            'placeholder': _("Nömrə"),'class':'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'placeholder': _("Şifrə"),'class':'form-control'})
        self.fields['retype_password'].widget = forms.PasswordInput(attrs={
            'placeholder': _("Şifrə təsdiqi"),'class':'form-control'})

    def clean(self):
        cleaned_data = super(EmployeeEditForm, self).clean()

        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('retype_password')

        user_email_obj = GUser.objects.filter(email=email).exclude(id=self.user_id)
        if user_email_obj:
            self._errors['email'] = _('Email is allready use')
        if user_email_obj:
            self._errors['username'] = _('Email is allready use')
        if password:
            if password and password_confirm:
                if password != password_confirm:
                    raise forms.ValidationError(_("Passwords not same"))
        return cleaned_data


class CurrencyForm(forms.ModelForm):

    class Meta:
        model = Currency
        fields = ('title', 'value', 'short_title',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'value': forms.TextInput(attrs={'class': 'form-control', }),
            'short_title': forms.TextInput(attrs={'class': 'form-control', }),
        }


# İncomeOutcomeForm
class IncomeOutcomeSearchForm(forms.Form):
    user = forms.ChoiceField(choices=[], label=_('Kimdən'), required=False, widget=forms.Select(
        attrs={'placeholder': _('Kimdən'), 'autocomplete': 'off', 'class': 'form-control', }))

    user_to = forms.ChoiceField(choices=[], label=_('Kimdən'), required=False, widget=forms.Select(
        attrs={'placeholder': _('Kimdən'), 'autocomplete': 'off', 'class': 'form-control' }))

    currency = forms.ChoiceField(choices=[], label=_('Valyuta'), required=False, widget=forms.Select(
        attrs={'placeholder': _('Valyuta'), 'autocomplete': 'off', 'class': 'form-control', }))
    type = forms.ChoiceField(choices=Form_io_type_choices, label=_('Tip'), required=False, widget=forms.Select(
        attrs={'placeholder': _('Tip'), 'autocomplete': 'off', 'class': 'form-control', }))

    title = forms.CharField(max_length=255, label=_('Başlıq'), min_length=2, required=False,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': _('Başlıq'), 'autocomplete': 'off',
                                            'class': 'form-control',}))

    amount_min = forms.DecimalField(max_digits=19, decimal_places=2, label=_('Məbləğ minimum'), required=False,
                                     widget=forms.NumberInput(
                                         attrs={'placeholder': _('Məbləğ minimum'), 'autocomplete': 'off',
                                                'class': 'form-control', }))

    amount_max = forms.DecimalField(max_digits=19, decimal_places=2, label=_('Məbləğ maksimum'), required=False,
                                     widget=forms.NumberInput(
                                         attrs={'placeholder': _('Məbləğ maksimum'), 'autocomplete': 'off',
                                                'class': 'form-control', }))
    start_date = forms.CharField(max_length=255, label=_('Başlanğıc tarix'), min_length=2, required=False,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': _('Başlanğıc tarix'), 'autocomplete': 'off',
                                            'class': 'form-control'}))
    end_date = forms.CharField(max_length=255, label=_('Son tarix'), min_length=2, required=False,
                               widget=forms.TextInput(attrs={'placeholder': _('Son tarix'), 'autocomplete': 'off',
                                                             'class': 'form-control', }))

    def __init__(self, *args, **kwargs):
        super(IncomeOutcomeSearchForm, self).__init__(*args, **kwargs)

        self.fields['user'].choices = [['', 'Hamısı']] + [[x.id, "{} {}".format(x.first_name,x.last_name)] for x in GUser.objects.filter()]
        self.fields['user_to'].choices = [['', 'Hamısı']] + [[x.id, "{} {}".format(x.first_name,x.last_name)] for x in GUser.objects.filter()]
        self.fields['currency'].choices = [['', 'Valyuta']] + [[x.id, x.short_title] for x in Currency.objects.filter(removed=False)]
        # self.fields['status'].choices = [[x.id, x.title] for x in PackageStatus.objects.filter()]
        # self.fields['outcome_type'].choices = [[x.id, x.title] for x in OutcomeType.objects.filter()]
        # self.fields['outcome_name'].choices = [[x.id, x.title] for x in OutcomeName.objects.filter()]
        # self.fields['outcome_type2'].choices = [[x.id, x.title] for x in OutcomeType2.objects.filter()]
        # self.fields['department'].choices = [[x.id, x.title] for x in Department.objects.filter(removed=False)]


# İncomeOutcomeForm
class IncomeOutcomeMainForm(forms.Form):
    user = forms.ChoiceField(choices=[], label=_('Kimdən'), required=True, widget=forms.Select(
        attrs={'placeholder': _('Kimdən'), 'autocomplete': 'off', 'class': 'form-control', }))

    user_to = forms.ChoiceField(choices=[], label=_('Kimdən'), required=True, widget=forms.Select(
        attrs={'placeholder': _('Kimdən'), 'autocomplete': 'off', 'class': 'form-control' }))

    title = forms.CharField(max_length=255, label=_('Başlıq'), min_length=2, required=False,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': _('Başlıq'), 'autocomplete': 'off',
                                            'class': 'form-control',}))


    type = forms.ChoiceField(choices=io_type_choices, label=_('Tip'), required=True, widget=forms.Select(
        attrs={'placeholder': _('Tip'), 'autocomplete': 'off', 'class': 'form-control', 'readonly': True, }))

    amount = forms.DecimalField(max_digits=19, decimal_places=2, label=_('Məbləğ'), required=True,
                                     widget=forms.NumberInput(
                                         attrs={'placeholder': _('Məbləğ'), 'autocomplete': 'off',
                                                'class': 'form-control', }))
    notes = forms.CharField(label=_('Qeydlər'), min_length=2, required=False, widget=forms.Textarea(
        attrs={'placeholder': _('Qeydlər'), 'autocomplete': 'off', 'class': 'form-control', 'rows': 3}))

    department = forms.ChoiceField(choices=[], label=_('Department'), required=False, widget=forms.Select(
        attrs={'placeholder': _('Department'), 'autocomplete': 'off', 'class': 'form-control', }))

    currency = forms.ChoiceField(choices=[], label=_('Valyuta'), required=True, widget=forms.Select(
        attrs={'placeholder': _('Valyuta'), 'autocomplete': 'off', 'class': 'form-control', }))
    date = forms.CharField(max_length=255, label=_('Ödəniş tarixi'), required=False, widget=forms.DateInput(
        attrs={'placeholder': _('Ödəniş tarixi'), 'autocomplete': 'off', 'class': 'form-control',
               }))


    outcome_type = forms.ChoiceField(choices=[], label=_('Xərcin Növü'), required=False, widget=forms.Select(
        attrs={'placeholder': _('Xərcin Növü'), 'autocomplete': 'off', 'class': 'form-control', }))

    outcome_name = forms.ChoiceField(choices=[], label=_('Xərcin Adı'), required=False, widget=forms.Select(
        attrs={'placeholder': _('Xərcin Adı'), 'autocomplete': 'off', 'class': 'form-control', }))

    outcome_type2 = forms.ChoiceField(choices=[], label=_('Xərcin Tipi'), required=False, widget=forms.Select(
        attrs={'placeholder': _('Xərcin Tipi'), 'autocomplete': 'off', 'class': 'form-control', }))

    def __init__(self, *args, **kwargs):
        super(IncomeOutcomeMainForm, self).__init__(*args, **kwargs)

        self.fields['user'].choices = [[x.id, "{} {}".format(x.first_name,x.last_name)] for x in GUser.objects.filter()]
        self.fields['user_to'].choices = [[x.id, "{} {}".format(x.first_name,x.last_name)] for x in GUser.objects.filter()]
        # self.fields['status'].choices = [[x.id, x.title] for x in PackageStatus.objects.filter()]
        self.fields['outcome_type'].choices = [['', 'Tipi']] + [[x.id, x.title] for x in OutcomeType.objects.filter()]
        self.fields['outcome_name'].choices = [['', 'Adı']] + [[x.id, x.title] for x in OutcomeName.objects.filter()]
        self.fields['outcome_type2'].choices = [['', 'Növü']] + [[x.id, x.title] for x in OutcomeType2.objects.filter()]
        self.fields['department'].choices =  [[x.id, x.title] for x in Department.objects.filter(removed=False)]
        self.fields['currency'].choices = [['', 'Valyuta']] + [[x.id, x.short_title] for x in Currency.objects.filter(removed=False)]
    def clean(self):
        cleaned_data = super(IncomeOutcomeMainForm, self).clean()
        department = cleaned_data.get('department')
        # if department <= 0:
        #     self._errors['pd_pay_amount'] = _('0 dan kiçik ola bilməz')

class IncomeOutcomeForm(forms.ModelForm):
    # outcome_name = forms.ModelChoiceField(required=False,queryset=OutcomeName.objects.all(), empty_label='Label')
    # outcome_name = forms.ChoiceField(required=False,widget=forms.Select(attrs={'class': 'form-control', }))
    # outcome_type2 = forms.ch(required=False,widget=forms.Select(attrs={'class': 'form-control', }))
    class Meta:
        model = IncomeOutcome
        fields = ('user', 'user_to', 'title','type','department','outcome_type','outcome_type2','outcome_name', 'amount', 'notes', 'date',)

        # exclude = ['outcome_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'user': forms.Select(attrs={'class': 'form-control', }),
            'user_to': forms.Select(attrs={'class': 'form-control', }),
            'type': forms.Select(attrs={'class': 'form-control', }),
            'department': forms.Select(attrs={'class': 'form-control', }),
            'outcome_type': forms.Select(attrs={'class': 'form-control', }),
            'outcome_type2': forms.Select(attrs={'class': 'form-control', }),
            'outcome_name': forms.Select(attrs={'class': 'form-control', }),
            'amount': forms.NumberInput(attrs={'class': 'form-control', }),
            'notes': forms.Textarea(attrs={'class': 'form-control', }),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', }),
        }


class CustomerNotesForm(forms.ModelForm):

    class Meta:
        model = CustomerNote
        fields = ('title', 'description',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'description': forms.Textarea(attrs={'class': 'form-control', }),
        }



class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
        }



class ProductTypeForm(forms.ModelForm):

    class Meta:
        model = ProductType
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
        }

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('title', 'address', 'ip',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': _("Başlıq") }),
            'address': forms.TextInput(attrs={'class': 'form-control','placeholder': _("Adres"), }),
            'ip': forms.TextInput(attrs={'class': 'form-control','placeholder': _("IP"), }),
        }



class EmployeePermitForm(forms.ModelForm):

    class Meta:
        model = EmployeePermit
        fields = ('employee', 'reason','description', 'day', 'time',)
        widgets = {
            'reason': forms.Select(attrs={'class': 'form-control','placeholder': _("Başlıq") }),
            'employee': forms.Select(attrs={'class': 'js-basic-single ', }),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder': _("Təsvir"), }),
            'day': forms.NumberInput(attrs={'class': 'form-control', }),
            'time': forms.TimeInput(attrs={'class': 'form-control', }),
        }


class PackageTypeForm(forms.ModelForm):

    class Meta:
        model = PackageType
        fields = ('title', 'description','type', 'month_count',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'description': forms.Textarea(attrs={'class': 'form-control', }),
            'type': forms.Select(attrs={'class': 'form-control', }),
            'month_count': forms.NumberInput(attrs={'class': 'form-control', }),
        }

class PackageOrderForm(forms.ModelForm):

    class Meta:
        model = PackageOrder
        fields = ('accepted', 'delivery_date', 'notes',)
        widgets = {
            'accepted': forms.CheckboxInput(attrs={'class': 'form-control', }),
            'delivery_date': forms.DateInput(attrs={'class': 'form-control', }),
            'notes': forms.Textarea(attrs={'class': 'form-control', }),
        }
import datetime
import decimal
import uuid

from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.db import models
from django.db.models import signals

from django.utils.translation import ugettext_lazy as _

# Create your models here.
from general.functions import path_and_rename

from django.utils import timezone

from panel.functions import monthdelta, months_between, change_data
from panel.tasks import package_utility_date

PERMIT_CHOİCE = (
    ("","Səbəb"),
    ("permit","İcaze"),
    ("late","Gecikmə"),
    ("penalty","Cərimə"),
)

class EmployeeSalary(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="+")
    month = models.IntegerField()
    year = models.IntegerField()
    work_minute = models.IntegerField(default=0)
    salary_amount = models.DecimalField("Miqdar",max_digits=19,decimal_places=2,default=0)
    result_amount = models.DecimalField("Miqdar",max_digits=19,decimal_places=2,default=0)
    penalty = models.DecimalField("Cərimə",max_digits=19,decimal_places=2,default=0)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} {}".format(self.employee.first_name,self.employee.last_name)
    class Meta:
        unique_together = ('employee', 'month', 'year',)


class EmployeePermit(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="+")
    reason = models.CharField(max_length=100,choices=PERMIT_CHOİCE)
    description = models.TextField(max_length=255)
    day = models.IntegerField()
    time  = models.TimeField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} {}".format(self.employee.first_name,self.employee.last_name)
    def get_reason(self):
        ret_val = ''
        for item in PERMIT_CHOİCE:
            if item[0] == self.reason:
                ret_val = item[1]
        return ret_val




GenderChoice = (
    ('','Cins'),
    ('man','Kişi'),
    ('woman','Qadın'),
)

class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    # father_name = models.CharField(_('Ata adi'), max_length=255, blank=True)
    serial_number = models.CharField(max_length=255)
    fin = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    gender = models.CharField(choices=GenderChoice,max_length=255,default='man')
    contact_number = models.CharField(max_length=255)
    birthdate = models.DateField(verbose_name="ad günü",blank=True,null=True)
    id_number = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(_('active'), default=True,)
    profile_picture = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
    passport_picture1 = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
    passport_picture2 = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
    department = models.ForeignKey('Department',blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    def get_phones(self):
        return CustomerPhoneNumber.objects.filter(customer=self)
    def get_packages_info(self):
        packs = Package.objects.filter(customer=self)
        return [packs.filter(status='active').count(),packs.exclude(status='active').count(),packs.all().count()]
    def __str__(self):
        return self.full_name
    def get_package_status(self):
        pack_list = Package.objects.filter(customer=self)
        active_packs = pack_list.filter(status__in=['active','waiting']).order_by('-first_date')
        not_active_packs = pack_list.exclude(status__in=['active','waiting']).order_by('-end_date')
        saled_packs = pack_list.filter(status='saled').order_by('-end_date')
        return_val = ['-','Paketi olmayıb','no-package','no-saled']
        if active_packs.count()>0:
            c_date = active_packs.first().first_date
            return_val = ["{}-{}-{} {}:{}".format(c_date.day,c_date.month,c_date.year,c_date.hour,c_date.minute,),'Aktiv','active']
        elif not_active_packs.count() > 0:
            if active_packs.first():
                c_date = active_packs.first().end_date
                return_val = ["{}-{}-{} {}:{}".format(c_date.day,c_date.month,c_date.year,c_date.hour,c_date.minute,),'Deaktiv','deactive']
            # else:
            #     c_date = active_packs.first().end_date
        if saled_packs.count() > 0:
            return_val.append('saled')
        else:
            return_val.append('no-saled')
        return return_val



class CustomerPhoneNumber(models.Model):
    customer = models.ForeignKey('Customer', blank=True, null=True)
    number = models.CharField(max_length=255)

    def __str__(self):
        return self.number


AnnuitetStatusChoice = (
    ('','Hamısı'),
    (1,'Annuitet'),
    (0,'Adi'),
)

PackageStatusChoice = (
    ('','Status'),
    ('active','Aktiv'),
    ('waiting','Yoxlamada'),
    ('paided','Bağlandı'),
    ('ordered','--- Sifarişə verildi'),
    ('closed','--- Təhvil verildi'),
    ('saled','Satıldı'),
)
ShowPhotoChoice = (
    ('hide','Gizlə'),
    ('show','Göstər'),
)
PackageStatusFormChoice = (
    ('','Status'),
    ('active','Aktiv'),
    ('waiting','Yoxlamada'),
    ('paided-all','Bağlandı'),
    ('paided', '--- Ödəmə tamamlandı'),
    ('ordered','--- Sifarişə verildi'),
    ('closed','--- Təhvil verildi'),
    ('saled','Satıldı'),
)

class PackageProduct(models.Model):
    package = models.ForeignKey('Package',blank=True,null=True)
    product_type = models.ForeignKey('ProductType',blank=True,null=True)
    product_amount = models.DecimalField("Miqdar",max_digits=10,decimal_places=2,default=0)
    date = models.DateTimeField(auto_now_add=True)




class PackageProductImage(models.Model):
    package = models.ForeignKey('Package',blank=True,null=True)
    image = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)




class Package(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="+",blank=True,null=True)
    customer = models.ForeignKey('Customer',blank=True,null=True)
    pledge_number = models.CharField(max_length=255,verbose_name="Girov nomresi")
    currency  = models.ForeignKey("Currency")

    first_date = models.DateTimeField(verbose_name="ilk tarix",blank=True,null=True)
    end_date = models.DateField(verbose_name="son tarix",blank=True,null=True)
    notes = models.TextField(blank=True,null=True)
    closed_reason = models.TextField(default='',blank=True,null=True)

    amount = models.DecimalField("Miqdar",max_digits=19,decimal_places=2)
    percent = models.DecimalField(max_digits=10,decimal_places=2)
    debt_amount = models.DecimalField("Qalan miqdar",max_digits=19,decimal_places=2,default=0.0)
    total_debt_extra = models.DecimalField("Qalan Faiz",max_digits=19,decimal_places=2,default=0.0)
    # amount_dollar = models.DecimalField("Miqdar",max_digits=19,decimal_places=2)
    # status = models.ForeignKey('PackageStatus', blank=True,null=True)
    status = models.CharField(max_length=100,default="",choices=PackageStatusChoice)

    packet_type = models.ForeignKey('PackageType')
    department = models.ForeignKey('Department')
    annuitet = models.BooleanField(default=False)

    product = models.ForeignKey('Product',blank=True,null=True)
    product_type = models.ForeignKey('ProductType',blank=True,null=True)
    product_amount = models.DecimalField("Miqdar",max_digits=10,decimal_places=2,default=0)
    last_payment_date = models.DateTimeField(blank=True,null=True)


    pay_date = models.DateField(verbose_name="odeme tarixi",blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    delay_day = models.IntegerField("Gecikmə",default=0)
    def __str__(self):
        return "{}-{}".format(self.id,self.customer.full_name)
    def get_last_order(self):
        return PackageOrder.objects.filter(package=self).order_by('-date').first()
    def get_last_daily_note(self):
        return PackageDailyNote.objects.filter(package=self).exclude(date__year=datetime.datetime.now().year,date__month=datetime.datetime.now().month,date__day=datetime.datetime.now().day,).order_by('-date').last()
    def get_last_payment(self):
        obj = PackagePaymentDates.objects.filter(package=self).order_by('-date').first()
        return obj.date + relativedelta(months=+1) if obj else self.first_date  + relativedelta(months=+1)
    def get_last_payment_real(self):
        obj = PackagePaymentDates.objects.filter(package=self).order_by('-date')
        mounth_count = 0
        for item in obj:
            mounth_count += item.month_count
        return self.first_date  + relativedelta(months=+(mounth_count+1))
    def get_pay_amount(self):
        return self.amount - self.debt_amount
    def get_monthly_percent(self):
        return self.debt_amount * self.percent / 100

def package_item_save(sender, instance, created, *args, **kwargs):
    # pass
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    if created:
        package_utility_date([instance.id])

#
signals.post_save.connect(package_item_save, sender=Package)


class PackageDailyNote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="+",blank=True,null=True)
    package = models.ForeignKey('Package',blank=True,null=True)
    content = models.CharField(max_length=255,blank=True,null=True,default='')
    date = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    removed = models.BooleanField(default=False)


class ProductType(models.Model):
    product = models.ForeignKey('Product',blank=True,null=True)
    title = models.CharField(max_length=255)
    removed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} - {}".format(self.id,self.product_id)


class PackageOrder(models.Model):
    package = models.ForeignKey('Package')
    accepted = models.BooleanField(default=False)
    delivery_date = models.DateField(blank=True,null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)


class WaitingPackage(models.Model):
    package = models.ForeignKey('Package')
    debt_amount = models.DecimalField("Qalan miqdar",max_digits=19,decimal_places=2,default=0.0)

    # start
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True,blank=True,null=True)
    def __str__(self):
        return "{}-{}".format(self.package.id, self.package.customer.full_name)


class PackagePaymentDates(models.Model):
    package = models.ForeignKey('Package')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="+",blank=True,null=True)
    delay_day = models.IntegerField("Gecikmə",default=0)
    paid_date = models.DateTimeField("Odənilen tarix")
    pay_date = models.DateTimeField("Odənməli tarix",blank=True,null=True)
    month_count = models.IntegerField("Ay Sayı",default=0)
    day_count = models.IntegerField("Gün Sayı",default=0)
    pay_amount = models.DecimalField("Odənilən miqdar",max_digits=19,decimal_places=2)
    calculated_percent = models.DecimalField("Hesablanmış faiz",max_digits=19,decimal_places=2,default=0.0)
    paid_percent = models.DecimalField("Faiz miqdarı",max_digits=19,decimal_places=2,default=0.0)
    percent_debt = models.DecimalField("Faiz Borcu",max_digits=19,decimal_places=2,default=0.0)
    penalty_amount = models.DecimalField("Cərimə",max_digits=19,decimal_places=2,default=0.0)
    description = models.CharField(max_length=500,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.package.customer.full_name
#
def package_payment_dates_save(sender, instance, created, *args, **kwargs):
    # pass
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    change_data(instance.package.id)
#
signals.post_save.connect(package_payment_dates_save, sender=PackagePaymentDates)
#

class PackageStatus(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Currency(models.Model):
    title = models.CharField(max_length=255)
    percent = models.DecimalField(max_digits=19,decimal_places=5,default=0)
    value = models.DecimalField(max_digits=19,decimal_places=5,default=1.0)

    short_title = models.CharField(max_length=10)
    removed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class CustomerNote(models.Model):
    customer = models.ForeignKey('Customer',related_query_name='notes')
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


PackageTypeChoice = (
    ('','-- Paket növü --'),
    ('daily','Gündəlik'),
    ('ten-daily','10 Gunluk'),
)
class PackageType(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(choices=PackageTypeChoice,max_length=255)
    month_count = models.PositiveIntegerField(default=1)
    description = models.TextField()
    removed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title



class Department(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=10)
    ip = models.CharField(max_length=255)
    removed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Log(models.Model):
    title = models.CharField(max_length=255)

    object = models.CharField(max_length=255)
    operation = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


reason_choices = (
    ("income", _("Mədaxil")),
    ("outcome", _("Məxaric")),
)
io_type_choices = (
    ("main", _("Əsas")),
    ("percent", _("Faiz")),
    ("office", _("Ofis")),
    ("credit", _("Kredit")),
    # ("outcome", _("Məxaric")),
)
Form_io_type_choices = (
    ("", _("Təyinat")),
    ("main", _("Əsas")),
    ("percent", _("Faiz")),
    ("office", _("Ofis")),
    ("credit", _("Kredit")),
    # ("outcome", _("Məxaric")),
)
class IncomeOutcome(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="+")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='+')
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='+',blank=True,null=True)
    title = models.CharField("Başlıq",max_length=255)
    reason = models.CharField(max_length=20,choices=reason_choices)
    type = models.CharField(max_length=20,choices=io_type_choices)
    amount = models.DecimalField("Miqdar",max_digits=19,decimal_places=2)
    currency = models.ForeignKey('Currency',blank=True,null=True)
    package_payment_date = models.ForeignKey('PackagePaymentDates',blank=True,null=True,on_delete=models.CASCADE)
    package = models.ForeignKey('Package',blank=True,null=True,on_delete=models.CASCADE)
    department = models.ForeignKey('Department',blank=True,null=True)
    notes = models.TextField()
    date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    outcome_type = models.ForeignKey("OutcomeType",blank=True,null=True,)
    outcome_name = models.ForeignKey("OutcomeName",blank=True,null=True)
    outcome_type2 = models.ForeignKey("OutcomeType2",blank=True,null=True)
    def __str__(self):
        return self.title

    def get_type(self):
        return_Val = ''
        for item in io_type_choices:
            if self.type == item[0]:
                return_Val = item[1]
                break
        return return_Val
    def get_amount(self):
        return_Val = 0.0
        if self.package_payment_date:
            if self.type == 'main':
                return_Val =  self.package_payment_date.pay_amount
            elif self.type == 'percent':
                return_Val =  self.package_payment_date.paid_percent
        elif self.package:
            return_Val =  self.package_payment_date.paid_percent
        else:
            return_Val = self.amount
        return "{0:.1f}".format(return_Val)
    def get_amount_currency(self):
        return_Val = 0.0
        if self.package_payment_date:
            if self.type == 'main':
                return_Val =  self.package_payment_date.pay_amount
            elif self.type == 'percent':
                return_Val =  self.package_payment_date.paid_percent
            currency = self.package_payment_date.package.currency.short_title
        elif self.package:
            return_Val =  self.package.amount
            currency = self.package.currency.short_title
        else:
            return_Val = self.amount
            currency = self.currency.short_title
        return "{} {}".format("{0:.1f}".format(return_Val),currency)



class OutcomeType(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class OutcomeName(models.Model):
    type = models.ForeignKey('OutcomeType',blank=True,null=True)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class OutcomeType2(models.Model):
    type_name = models.ForeignKey('OutcomeName',blank=True,null=True)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

import logging

class LogOnUpdateDeleteMixin(models.Model):
    pass

    def delete(self, *args, **kwargs):
        super(LogOnUpdateDeleteMixin, self).delete(*args, **kwargs)
        logging.info("%s instance %s (pk %s) deleted" % (str(self._meta), str(self), str(self.pk),)) # or whatever you like

    def save(self, *args, **kwargs):
        super(LogOnUpdateDeleteMixin, self).save(*args, **kwargs)
        logging.info("%s instance %s (pk %s) updated" % (str(self._meta), str(self), str(self.pk),)) # or whatever you like

    class Meta:
        abstract = True






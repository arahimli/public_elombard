from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from base_user.tools.common import  GENDER, USERTYPES, slugify
from general.functions import path_and_rename, send_html_mail
from datetime import datetime as d
import calendar
from django.db.models import Q, signals
# from work.common import *
# My custom tools import
from datetime import datetime, timedelta


# Create your models here.
USER_MODEL = settings.AUTH_USER_MODEL
import random
import uuid




# Customize User model
class MyUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username, password and email are required. Other fields are optional.
    """

    username = models.CharField(_('username'), max_length=100, unique=True,
                                help_text=_('Tələb olunur. 75 simvol və ya az. Hərflər, Rəqəmlər və '
                                            '@/./+/-/_ simvollar.'),
                                # validators=[
                                #     validators.RegexValidator(r'^[\w.@+-]+$', _('Düzgün istifadəçi adı daxil edin.'),
                                #                               'yanlışdır')
                                # ]
                                )
    first_name = models.CharField(_('first name'), max_length=255, blank=True)
    last_name = models.CharField(_('last name'), max_length=255, blank=True)
    email = models.EmailField(_('email address'), max_length=255,unique=True)
    salary = models.DecimalField("Maaş",max_digits=19,decimal_places=2,default=0.0)
    # birthdate = models.DateField(verbose_name="ad günü",blank=True,null=True)
    profile_picture = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
    passport_picture1 = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
    passport_picture2 = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
    verified = models.BooleanField(default=False, verbose_name="Təstiqlənmə")
    phone = models.CharField(max_length=100, verbose_name="Telefonu", null=True, blank=True)
    department = models.ForeignKey('panel.Department',blank=True,null=True,related_name="+")
    permissions_department = models.ManyToManyField('panel.Department',blank=True,null=True,related_name='+')
    slug = models.SlugField(null=True, blank=True)


    usertype = models.IntegerField(choices=USERTYPES, verbose_name="User Type", null=True, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    """
        Important non-field stuff
    """
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'İstifadəçi'
        verbose_name_plural = 'İstifadəçilər'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def save(self, *args, **kwargs):
        super(MyUser, self).save(*args, **kwargs)
        self.slug = slugify(self.first_name+str(timezone.now().timestamp()).replace('.','-'))
        super(MyUser, self).save(*args, **kwargs)
    # def permissions(self):
    #     return_list = []
    #     for item in UserPermission.objects.filter(user=self):
    #         return_list.append(item.permission)
    #     return return_list

def user_save(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        # print(signal)
        # Send verification email
        confirm_obj = UserConfrimationKeys(key=uuid.uuid4(),user=instance,expired_date=datetime.now()+timedelta(days=7),expired=False)
        confirm_obj.save()
        try:
            send_html_mail(instance.email,_("Confirm email"),'<a href="{}">{}</a>'.format(reverse('base-user:confirm-account',kwargs={'username':instance.username,'key':confirm_obj.key}),_('Confirm your account,click here')))
        except:
            pass

signals.post_save.connect(user_save, sender=MyUser)


class UserConfrimationKeys(models.Model):
    key = models.CharField(max_length=255,null=True, blank=True)
    user = models.ForeignKey('MyUser', null=True,blank=True)
    expired_date = models.DateTimeField()
    expired = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date',)
        verbose_name = "Təstiqlənmiş user"
        verbose_name_plural = "Təstiqlənmiş userlər"

    def __str__(self):
        return "%s" % self.key

#
#
# class UserPermission(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL)
#     permission = models.CharField(choices=rule_models_choices,max_length=255)
#     class Meta:
#         unique_together = ("user", "permission")



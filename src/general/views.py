import datetime
from django.shortcuts import render

# Create your views here.
from elombard import settings


def base(req=None):

    data = {
        'now':datetime.datetime.now(),
        'base_site_name' : settings.SITE_NAME,
        'non_operate' : ['waiting','paided','ordered','closed','saled'],
        # 'base_categories':Menu.objects.filter(status=True,menu_type='dynamic-menu').filter(parent=None).order_by('order_index'),
        # 'base_categories':Menu.objects.filter(status=True,menu_type='dynamic-menu').filter(parent=None).order_by('order_index'),
    }
    return data

def base_auth(req=None):

    data = {
        'now':datetime.datetime.now(),
        'base_site_name' : settings.SITE_NAME,
        # 'base_categories':Menu.objects.filter(status=True,menu_type='dynamic-menu').filter(parent=None).order_by('order_index'),
        'base_profile' : req.user,
        'non_operate' : ['waiting','paided','ordered','closed','saled'],
    }
    return data



import random
import string
import copy

from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext as _

from celery.task import task
from celery import shared_task,current_task
import googlemaps
from datetime import datetime

# from content.models import LocationDistance
# from general.read_customer import read_customer_from_excel as general_read_customer_from_excel
# from .main_functions import *



@shared_task
def add_location_from_excel_list(url):
    from django.core.mail import EmailMultiAlternatives

    subject, from_email, to = _('confirmation'), settings.EMAIL_HOST_USER, 'to@example.com'
    text_content = 'This is an important message.'
    html_content = '<a href="{}"><strong>{}</strong></a>'.format('sds',_('Please click this link and confirm account'))
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return '{} customers created with success!'.format('succes')
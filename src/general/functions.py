from django.conf import settings
from celery import shared_task
from django.contrib.admin.widgets import AdminFileWidget
from django.utils import timezone
import os
from uuid import uuid4

from django.utils.datetime_safe import datetime as datetime_util
from django.utils.safestring import mark_safe
import datetime



class ImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            output.append(('<a target="_blank" href="%s">'
                           '<img src="%s" height="200" title="%s"/></a> '
                           % (value.url, value.url, value.name)))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))




def path_and_rename(instance, filename):
    now = datetime_util.now()
    upload_to = 'photos/{}/{}/{}'.format(now.year,now.month,now.day)
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}-{}.{}'.format(uuid4().hex,instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

#
# def path_and_rename_spec(path):
#     def wrapper(instance, filename):
#         try :
#             ext = filename.split('.')[-1]
#             ext = str(ext).lower()
#         except:
#             ext = filename.split('.')[-1]
#         # get filename
#         if instance.pk:
#             filename = '{}-{}.{}'.format(uuid4().hex, instance.pk, ext)
#         else:
#             # set filename as random string
#             filename = '{}.{}'.format(uuid4().hex, ext)
#         # return the whole path to the file
#         return os.path.join(path, filename)
#     return wrapper
#


@shared_task
def send_html_mail(email,subject,html):
    from django.core.mail import send_mail
    from django.conf import settings
    send_mail(
        subject=subject,
        html_message=html,
        message='',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False
    )
    return True
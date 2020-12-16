import datetime

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.utils.deprecation import MiddlewareMixin

from uuid import getnode as get_mac
def get_mac_address(request):
    mac = get_mac()
    # return '\n'.join(url.format(year) for year in range(2000, 2016))
    return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class FilterIPMiddleware(MiddlewareMixin):
    # Check if client IP is allowed
    def process_request(self, request):
        # allowed_ips = ['192.168.1.1', '123.123.123.123',] # Authorized ip's
        # ip = request.META.get('REMOTE_ADDR') # Get client IP
        now = datetime.datetime.now()
        # if ip not in allowed_ips:
        # print(now.hour)
        # print(get_client_ip(request))
        # print(get_mac_address(request))
        # if request.user.is_anonymous():
        #     pass
        # elif now.hour >= 18 and request.user.usertype == 2 and request.user.department.ip != get_client_ip(request):
        #     print(request.user)
        #     raise PermissionDenied    # If user is not allowed raise Error

        # return None

from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns

from .views import *


urlpatterns = [
	url(r'^login/$', log_in, name='login'),
	url(r'^register/$', signup, name='register'),
	url(r'^confirm-account/(?P<username>\w+)/(?P<key>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)$', confirm_account, name='confirm-account'),
	url(r'^logout/$', log_out, name='logout'),

]

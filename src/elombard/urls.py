"""examapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.utils import translation
from django.views import generic
from django.views.static import serve

# from content.views import dashboard
from home.views import *
from django.views import static
from django.conf import settings
# from general import set_lang as core_views


urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', admin.site.urls,name="admin"),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT }, name='media'),
]

translation.activate(settings.LANGUAGE_CODE)

# urlpatterns += i18n_patterns(
urlpatterns += [

    # url(r'^', include("home.urls", namespace="home")),
    url(r'^', include("panel.urls", namespace="panel")),
    # url(r'^', include("content.urls", namespace="content")),

    url(r'^auth/', include("base_user.urls", namespace="base-user")),

]

urlpatterns += staticfiles_urlpatterns()




@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)


if settings.DEBUG is False:   #if DEBUG is True it will be served automatically
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT }, name='static'),
        url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT }, name='media')
    ]
urlpatterns += staticfiles_urlpatterns()
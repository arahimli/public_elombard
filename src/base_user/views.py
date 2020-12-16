from django.shortcuts import render, get_object_or_404
import hashlib
import random

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext as _
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
# from flynsarmy_paginator.paginator import FlynsarmyPaginator
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, get_user_model, logout

from base_user.forms import LoginForm, UserRegistrationForm
from base_user.models import UserConfrimationKeys
from general.views import base
GUser = get_user_model()

# Create your views here.
def log_out(request):
    if request.user.is_authenticated():
        logout(request)
    # next_url = request.GET.get('next_url')
    # if next_url:
    #     pass
    # else:
    next_url = reverse('base-user:login')
    return HttpResponseRedirect(next_url)

def confirm_account(request,username,key):
    context = base(req=request)
    confirm_obj = get_object_or_404(UserConfrimationKeys,user__username=username,key=key,expired_date__gte=datetime.now(),expired=False)
    confirm_obj.expired = True
    confirm_obj.user.is_active = True
    confirm_obj.user.save()
    confirm_obj.save()
    # next_url = request.GET.get('next_url')
    # if next_url:
    #     pass
    # else:
    context['message'] = _('Your account has been confirmed successfully')
    response = render(request, 'base-user/confirm.html', context=context)
    return response


def signup(request):
    signup_form = UserRegistrationForm(request.POST or None)
    context = base(req=request)
    if request.method == 'POST':
        if signup_form.is_valid():
            clean_data = signup_form.cleaned_data
            name = clean_data.get('name')
            surname = clean_data.get('surname')
            username = clean_data.get('username')
            email = clean_data.get('email')
            phone = clean_data.get('phone')
            password = clean_data.get('password')
            retype_password = clean_data.get('retype_password')

            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]

            # activation_key = hashlib.sha1(salted).hexdigest()
            #
            # key_expires = datetime.datetime.today() + datetime.timedelta(1)
            password = make_password(password, salt=salt)

            user_obj = GUser(first_name=name,last_name=surname,email=email, username=username, phone=phone, password=password, usertype=3, is_active=False)
            user_obj.save()
            context['signup_message'] = _('Please confirm your email')
            signup_form = UserRegistrationForm()

    context['signup_form'] = signup_form
    response = render(request, 'base-user/signup.html', context=context)
    return response

def log_in(request):
    login_form = LoginForm(request.POST or None)
    context = base(req=request)
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('panel:dashboard'))
    context['login_form'] = login_form
    next_url = request.GET.get('next_url')
    context['next_url'] = next_url
    # return HttpResponse(next_url)
    message_login = ''
    if request.method == 'POST':
        if login_form.is_valid():
            clean_data = login_form.cleaned_data
            email = clean_data.get('lemail')
            password = clean_data.get('lpassword')
            remember_me = clean_data.get('remember_me')

            # if remember_me:
            #     remember_me = True
            # else:
            #     remember_me = False

            print('valid')
            try:
                # user_email = GUser.objects.get(email=email)
                # print("user_email={}".format(user_email.username))
                a_user = auth.authenticate(username=email,password=password)
                if a_user is not None:
                    if a_user.is_active:
                        print("user.is_active")
                        auth.login(request, a_user)
                        # return HttpResponse(next_url)
                        if next_url =='None' or not next_url:
                            next_url = reverse('panel:dashboard')
                        else:
                            pass
                        # return HttpResponse(next_url)
                        message_login = _("you are logined")
                        print(message_login)
                        return HttpResponseRedirect(next_url)
                    else:
                        print("user.is_active not ")
                        message_login = _("Please wait for confirmed account")
                else:
                    message_login = _("Email or password is incorrect")
                    print("----------------------------------------------------------------------------------------")
                    print(message_login)
            except:
                message_login = _("Email or password is incorrect")
                print("----------------------------------------------------------------------------------------")
                print(message_login)

            # else:
            #     # print("user.is_active not")
            #     # print(a_user)
            #     message_login = _("email_or_password_incorrect")

        context['message_login'] = message_login
    response = render(request, 'base-user/signin.html', context=context)
    return  response


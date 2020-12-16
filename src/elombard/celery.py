import os

from celery import Celery, shared_task
from celery.schedules import crontab
import datetime

import requests
from dateutil.relativedelta import relativedelta
from django.db.models import Q
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elombard.settings')

app = Celery('elombard')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.timezone = 'Asia/Baku'





# @app.task
@shared_task
def first_dask_date_phonenumber():
    import datetime
    from dateutil.relativedelta import relativedelta
    from django.db.models import Q
    # from django.shortcuts import get_object_or_404

    from panel.models import CustomerPhoneNumber
    from django.db.models import Min
    # First select the min ids
    min_id_objects = CustomerPhoneNumber.objects.values('customer_id', 'number').annotate(minid=Min('id'))
    min_ids = [obj['minid'] for obj in min_id_objects]
    # Now delete
    CustomerPhoneNumber.objects.exclude(id__in=min_ids).delete()

    print("task tasktask tasktask task __________________________________________ task tasktask tasktask task ")
    return 'first_time'





# @app.task
@shared_task
def first_time_income_outcome():
    import datetime
    from dateutil.relativedelta import relativedelta
    from django.db.models import Q
    # from django.shortcuts import get_object_or_404

    now = timezone.now()
    from panel.models import PackagePaymentDates, IncomeOutcome, Package
    package_payment_dates = PackagePaymentDates.objects.all().order_by('date')
    packages = Package.objects.all().order_by('date')
    IncomeOutcome.objects.all().delete()
    for package_payment_dates_obj in package_payment_dates:
        if package_payment_dates_obj.paid_percent > 0:
            IncomeOutcome_obj = IncomeOutcome(
                author_id = package_payment_dates_obj.user_id if package_payment_dates_obj.user else 5,
                user_id = package_payment_dates_obj.user_id if package_payment_dates_obj.user else 5,
                author = package_payment_dates_obj.user,
                user = package_payment_dates_obj.user,
                title = '{}{}'.format(package_payment_dates_obj.package.customer.full_name,' - Faiz odeme'),
                reason = 'income',
                type = 'percent',
                amount = package_payment_dates_obj.paid_percent,
                package_payment_date = package_payment_dates_obj,
                notes = '{} {}'.format(package_payment_dates_obj.package.customer.full_name,' - Faiz odeme'),
                date=package_payment_dates_obj.paid_date,
                department=package_payment_dates_obj.package.department,
                currency=package_payment_dates_obj.package.currency,
            )
            IncomeOutcome_obj.save()
        if package_payment_dates_obj.pay_amount > 0.0:
            IncomeOutcome_obj = IncomeOutcome(
                author_id = package_payment_dates_obj.user_id if package_payment_dates_obj.user else 5,
                user_id = package_payment_dates_obj.user_id if package_payment_dates_obj.user else 5,
                title = '{}{}'.format(package_payment_dates_obj.package.customer.full_name,' - Azaltma etmək'),
                reason = 'income',
                type = 'main',
                amount = package_payment_dates_obj.pay_amount,
                package_payment_date = package_payment_dates_obj,
                notes = '{} {}'.format(package_payment_dates_obj.package.customer.full_name,' - Azaltma etmək'),
                date=package_payment_dates_obj.paid_date,
                department=package_payment_dates_obj.package.department,
                currency=package_payment_dates_obj.package.currency,
            )
            IncomeOutcome_obj.save()
    for package_obj in packages:
        IncomeOutcome_obj = IncomeOutcome(
            author_id = package_obj.user_id if package_obj.user else 5,
            user_id = package_obj.user_id if package_obj.user else 5,
            title = '{}{}'.format(package_obj.customer.full_name,' - Faiz odeme'),
            reason = 'outcome',
            type = 'credit',
            amount = package_obj.amount,
            package = package_obj,
            notes = '{} {}'.format(package_obj.customer.full_name,' - Faiz odeme'),
            date=package_obj.first_date,
            department=package_obj.department,
            currency=package_obj.currency,
        )
        IncomeOutcome_obj.save()



# @app.task
@shared_task
def first_time():
    import datetime
    from dateutil.relativedelta import relativedelta
    from django.db.models import Q
    # from django.shortcuts import get_object_or_404

    from panel.models import PackagePaymentDates
    package_payment_dates = PackagePaymentDates.objects.exclude(delay_day__gte=0).order_by('date')
    for package_payment_date_item in package_payment_dates:
        if package_payment_date_item.delay_day < 0:
            package_payment_date_item.delay_day = package_payment_date_item.delay_day * (-1)
            package_payment_date_item.save()

    print("task tasktask tasktask task __________________________________________ task tasktask tasktask task ")
    return 'first_time'


# @app.task
@shared_task
def daily_dask_date():
    import datetime
    from dateutil.relativedelta import relativedelta
    from django.db.models import Q
    # from django.shortcuts import get_object_or_404

    from panel.models import PackagePaymentDates
    from panel.models import  Package
    now = datetime.datetime.now()
    for package_item in Package.objects.filter(Q(status='active') | Q(status='waiting')):
        id = package_item.id

        package_item.last_payment_date = package_item.get_last_payment_real()
        package_payment_dates = PackagePaymentDates.objects.filter(package_id=id).order_by('date')
        paid_amount = 0.0
        # percent_amount = 0.0
        paid_percent_amount = 0.0
        calculated_percent_amount = 0.0
        month_count = 0
        paid_amount_no_paid_date = package_item.first_date.date()
        for package_payment_date_item in package_payment_dates:
            paid_amount += float(package_payment_date_item.pay_amount)
            calculated_percent_amount += float(package_payment_date_item.calculated_percent)
            paid_percent_amount += float(package_payment_date_item.paid_percent)
            month_count += package_payment_date_item.month_count
        percent_debt_amount = calculated_percent_amount - paid_percent_amount
        paid_amount_no_paid_date += relativedelta(months=+month_count)
        # print("percent_debt_amountpercent_debt_amountpercent_debt_amoun

        print("percent_debt_amountpercent_debt_amountpercent_debt_amountpercent_debt_amountpercent_debt_amount")
        print(percent_debt_amount)
        print(paid_amount_no_paid_date)
        print(now)
        print("percent_debt_amountpercent_debt_amountpercent_debt_amountpercent_debt_amountpercent_debt_amount")

        if percent_debt_amount <= 0 and package_item.debt_amount <= 0:
            package_item.status = 'paided'
            package_item.delay_day = 0
        else:
            if package_item.status == 'paided':
                package_item.status = 'active'
        package_item.debt_amount = float(package_item.amount) - paid_amount
        package_item.save()
        package_item_status = package_item.status
        i_countet = 0

        delay_paid_date = paid_amount_no_paid_date + relativedelta(months=+1)
        dif_date = now.date() - delay_paid_date
        package_item.delay_day = dif_date.days if dif_date.days >= 0 else 0
        package_item.save()

    print("task tasktask tasktask task ------------------------------ task tasktask tasktask task ")
    return 'data'




# @app.task
@shared_task
def daily_dask_date_3():
    import datetime
    from dateutil.relativedelta import relativedelta
    from django.db.models import Q
    # from django.shortcuts import get_object_or_404

    from panel.models import PackagePaymentDates
    from panel.models import  Package
    now = datetime.datetime.now()


    package_payment_dates = PackagePaymentDates.objects.filter().order_by('date')
    for item in package_payment_dates:
        item.percent_debt = item.paid_percent - item.calculated_percent
        item.save()

# @app.task
@shared_task
def daily_dask_date_2():
    import datetime
    from dateutil.relativedelta import relativedelta
    from django.db.models import Q
    # from django.shortcuts import get_object_or_404

    from panel.models import PackagePaymentDates
    from panel.models import  Package
    now = datetime.datetime.now()
    for package_item in Package.objects.exclude(Q(status='active') | Q(status='waiting')):
        id = package_item.id
        package_payment_dates = PackagePaymentDates.objects.filter(package_id=id).order_by('date')
        paid_amount = 0.0
        # percent_amount = 0.0
        paid_percent_amount = 0.0
        calculated_percent_amount = 0.0
        paid_amount_no_paid_date = package_item.first_date.date()
        for package_payment_date_item in package_payment_dates:
            paid_amount += float(package_payment_date_item.pay_amount)
            calculated_percent_amount += float(package_payment_date_item.calculated_percent)
            paid_percent_amount += float(package_payment_date_item.paid_percent)
            paid_amount_no_paid_date += relativedelta(months=+package_payment_date_item.month_count)
        percent_debt_amount = calculated_percent_amount - paid_percent_amount

        package_item.debt_amount = float(package_item.amount) - paid_amount
        # package_item.save()
        # package_item_status = package_item.status
        # i_countet = 0

        # delay_paid_date = paid_amount_no_paid_date + relativedelta(months=+1)
        # dif_date = now.date() - delay_paid_date
        package_item.delay_day = 0
        package_item.save()

        print("------------------------------* package_item_status *------------------------------")
        print(percent_debt_amount)
        print(package_item.status)
        print(package_item.id)
        print("------------------------------* package_item_status *------------------------------")
    print("________________________________________________* task3 *________________________________________________")
    return 'data'


import datetime

app.conf.beat_schedule = {
    # "see-you-in-ten-seconds-task": {
    #     "task": "elombard.celery.see_youso",
    #     "schedule": 10.0,
    #     "args": [],
    # },
    "daily-dask-date-in-twenty-seconds-task": {
        "task": "elombard.celery.daily_dask_date",
        # "schedule": 250.0,
        # "schedule": 3.0,
        # 'schedule': datetime.timedelta(seconds=400), # 300 = every 5 minutes
        # "schedule": crontab(minute='*/5'),
        "schedule": crontab(hour=0, minute=35),
        "args": [],
    },
    # "daily-dask-date-in-twenty-seconds-task1": {
    #     "task": "elombard.celery.daily_dask_date",
    #     # "schedule": 250.0,
    #     # "schedule": 3.0,
    #     # 'schedule': datetime.timedelta(seconds=400), # 300 = every 5 minutes
    #     # "schedule": crontab(minute='*/5'),
    #     "schedule": crontab(hour=14, minute=45),
    #     "args": [],
    # },
    # "daily-dask-date-in-twenty-seconds-task-phonenumber": {
    #     "task": "elombard.celery.first_dask_date_phonenumber",
    #     # "schedule": 250.0,
    #     # "schedule": 3.0,
    #     # 'schedule': datetime.timedelta(seconds=400), # 300 = every 5 minutes
    #     # "schedule": crontab(minute='*/5'),
    #     "schedule": crontab(hour=17, minute=15),
    #     "args": [],
    # },
    # "daily-dask-date-in-twenty-seconds-first_time_income_outcome": {
    #     "task": "elombard.celery.first_time_income_outcome",
    #     # "schedule": 250.0,
    #     # "schedule": 3.0,
    #     # 'schedule': datetime.timedelta(seconds=400), # 300 = every 5 minutes
    #     # "schedule": crontab(minute='*/5'),
    #     "schedule": crontab(hour=9, minute=38),
    #     "args": [],
    # },
    "daily-dask-date-in-twenty-seconds-daily_dask_date_2": {
        "task": "elombard.celery.daily_dask_date_2",
        # "schedule": 250.0,
        # "schedule": 3.0,
        # 'schedule': datetime.timedelta(seconds=400), # 300 = every 5 minutes
        # "schedule": crontab(minute='*/5'),
        "schedule": crontab(hour=14, minute=3),
        "args": [],
    },
    # "daily-dask-date-in-twenty-seconds-task2": {
    #     "task": "elombard.celery.first_time",
    #     # "schedule": 250.0,
    #     # "schedule": 3.0,
    #     # 'schedule': datetime.timedelta(seconds=400), # 300 = every 5 minutes
    #     # "schedule": crontab(minute='*/5'),
    #     # "schedule": crontab(hour=10, minute=18),
    #     "args": [],
    # },
    # "daily-dask-date-in-twenty-seconds-task3": {
    #     "task": "elombard.celery.daily_dask_date",
    #     # "schedule": 250.0,
    #     # "schedule": 3.0,
    #     # 'schedule': datetime.timedelta(seconds=400), # 300 = every 5 minutes
    #     # "schedule": crontab(minute='*/5'),
    #     "schedule": crontab(hour=9, minute=30),
    #     "args": [],
    # },
    # "daily-dask-date-in-twenty-seconds-task2": {
    #     "task": "elombard.celery.daily_dask_date_2",
    #     # "schedule": 250.0,
    #     # "schedule": 3.0,
    #     'schedule': datetime.timedelta(seconds=400), # 300 = every 5 minutes
    #     # "schedule": crontab(minute='*/5'),
    # #     "schedule": crontab(hour=13, minute=20),
    #     "args": [],
    # },
}

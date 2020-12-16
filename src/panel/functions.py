import decimal
from calendar import monthrange
from datetime import datetime, timedelta
from django.utils import timezone

from dateutil.relativedelta import relativedelta



def monthdelta(d1, d2):
    delta = 0
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 += timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta

import datetime as dt


def months_between(date1,date2):
    print("date1,date2 - {} , {}".format(date1,date2))
    if date1>date2:
        date1,date2=date2,date1
    m1=date1.year*12+date1.month
    m2=date2.year*12+date2.month
    months=m2-m1
    if date1.day>date2.day:
        months-=1
    elif date1.day==date2.day:
        seconds1=date1.hour*3600+date1.minute+date1.second
        seconds2=date2.hour*3600+date2.minute+date2.second
        if seconds1>seconds2:
            months-=1
    return months

def change_data(id):
    from panel.models import PackagePaymentDates, Package
    package_item = Package.objects.get(id=id)
    print("-%-%-%-%-%-% res_delay_day = {}".format(package_item.delay_day))
    total_amount = decimal.Decimal(0)
    total_month = 0
    total_day = 0
    now = timezone.now()
    # res_delay_day = 0
    print("%$%$%$%$%$%$%-%$%$%$%$%$%$%-%$%$%$%$%$%$%-%$%$%$%$%$%$%-%$%$%$%$%$%$%-%$%$%$%$%$%$%")
    print(package_item.first_date)
    dif_date_month = months_between(package_item.first_date,now, )
    print("666666666666666666666666666666666666666666666666666666666666666666666666666666")
    r = relativedelta(now.date(),package_item.first_date.date())
    r.months * (r.years+1)
    print(r.months * (r.years+1))
    print(r.months )
    print((r.years+1))
    print(dif_date_month)
    print("666666666666666666666666666666666666666666666666666666666666666666666666666666")
        # (now.date() -
        #         package_item.first_date ).months
    objs = PackagePaymentDates.objects.filter(package=package_item)
    for obj_item in objs:
        # if obj_item.paid:
        total_month += obj_item.month_count
        total_day += obj_item.day_count
    if now.date() > package_item.first_date.date() + relativedelta(months=+(total_month+1)) + timedelta(days=total_day):
        print("-------------------------------******-*****------------------------------")
        print(package_item.first_date.date() +
                                        relativedelta(months=+(total_month+1)))
        print(now.date())
        # print(now.date()+datetime.timedelta(days=1))
        res_delay_day = (now.date() - (package_item.first_date.date() +
                                        relativedelta(months=+(total_month+1)))).days - total_day

    else:
        res_delay_day = 0

    print("*_*_* res_delay_day = {}".format(res_delay_day))
    # package_item.delay_day = res_delay_day
    print("*_*_* res_delay_day = {}".format(package_item.delay_day))
    # package_item.save()
    Package.objects.filter(id=id).update(delay_day = res_delay_day)
    package_item2 = Package.objects.get(id=id)
    print("*-*-* res_delay_day *-*-**-*-**-*-**-*-**-*-**-*-**-*-**-*-**-*-*")
    print("*-*-* res_delay_day = {}".format(package_item2.delay_day))
    print("*-*-* res_delay_day = {}".format(package_item2.id))


def package_utility_date(id_list):
    import datetime
    from dateutil.relativedelta import relativedelta
    from django.db.models import Q
    # from django.shortcuts import get_object_or_404

    from panel.models import PackagePaymentDates, Package, IncomeOutcome
    now = datetime.datetime.now()
    for package_item in Package.objects.filter(id__in=id_list).filter(Q(status='active') | Q(status='waiting')):
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

        print("percent_debt_amountpercent_debt_amountpercent_debt_amountpercent_debt_amountpercent_debt_amount")
        print(percent_debt_amount)
        print("percent_debt_amountpercent_debt_amountpercent_debt_amountpercent_debt_amountpercent_debt_amount")

        if percent_debt_amount <= 0 and package_item.debt_amount <= 0:
            package_item.status = 'paided'
            package_item.delay_day = 0
        else:
            if package_item.status == 'paided':
                package_item.status = 'active'
        package_item.save()
        package_item_status = package_item.status
        i_countet = 0

        delay_paid_date = paid_amount_no_paid_date + relativedelta(months=+1)
        dif_date = now.date() - delay_paid_date
        package_item.delay_day = dif_date.days if dif_date.days >= 0 else 0
        package_item.save()
        IncomeOutcome(
            author=package_item.user,
            package=package_item,
            title="yeni paket {}"
        )

    print("task tasktask tasktask task ------------------------------ task tasktask tasktask task ")
    return 'data'
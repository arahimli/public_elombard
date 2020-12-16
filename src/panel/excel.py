import datetime
import uuid

import xlrd

azn_ids = {}
usd_ids = {}

def check_(item,list_s):
    result = [False,None]
    for it in list_s:
        if item in it or it in item:
            result = [True,it]
            break
    return result


loc = ("l1-az.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
for_i = 0
customer_sql = ''
packages_sql = ''
numbers_sql = ''
numbers_id = 0
data_customer = {}
data_customer_list = []
data_customer_list_dict = {}
for_customer_i = 10
last_index = 0
status_bar = {
    'BAGLANDI':'closed',
    'ACILDI':'saled',
    'SATILDI':'saled',
    'AKTIV':'active',
    'YOXLAMA':'waiting',
}

for i in range(sheet.nrows):
    for_i += 1
    if for_i > 2:

        try:
            # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            # print(sheet.cell_value(i, 1))
            # print(sheet.cell_value(i, 0))
            # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            serial_sate = float(sheet.cell_value(i, 1))
            seconds = (serial_sate - 25569) * 86400.0
            serial_first_date = float(sheet.cell_value(i, 5))
            seconds_first_date = (serial_first_date - 25569) * 86400.0
            try:
                serial_end_date = float(sheet.cell_value(i, 6))
                seconds_end_date = (serial_end_date - 25569) * 86400.0
            except:
                seconds_end_date = 0
            # print(datetime.datetime.utcfromtimestamp(seconds))
            # print(str(sheet.cell_value(i, 4)).strip()
            #       )
            # print(data_customer_list)
            pack_data_item = {
                'id':sheet.cell_value(i, 0),
                'customer_id':'',
                'pledge_number':sheet.cell_value(i, 3),
                'currency':1,
                'first_date':sheet.cell_value(i, 5),
                'end_date':sheet.cell_value(i, 6),
                'amount':sheet.cell_value(i, 7),
                'percent':sheet.cell_value(i, 8),
                'debt_amount':sheet.cell_value(i, 7),
                'total_debt_extra':0,
                'status':sheet.cell_value(i, 9),
                'packet_type':sheet.cell_value(i, 0),
                'department':1,
                'notes':sheet.cell_value(i, 0),
                'annuitet':False,
                'date':sheet.cell_value(i, 1),
                'delay_day':0,
            }
            if_check_item = check_(str(sheet.cell_value(i, 4)).strip() , data_customer_list)
            if if_check_item[0] == False:
                data_customer_list_dict["{}".format(str(sheet.cell_value(i, 4)).strip())] = len(data_customer_list)+3
                # print("--------------------------------------------------------------------------")
                # print(data_customer_list_dict["{}".format(str(sheet.cell_value(i, 4)).strip())])
                # print(str(sheet.cell_value(i, 4)).strip())
                # print("--------------------------------------------------------------------------")
                customer_sql = "{}{}".format(customer_sql,"INSERT INTO `panel_customer` VALUES({}, '{}', 'az12345678', '{}', '{}', '{}', '{}','{}', 1, '', '', '', '{}', 1, 'man');".format(
                    len(data_customer_list)+3,
                    str(sheet.cell_value(i, 4)).strip(),
                    'fin',
                    'address',
                    sheet.cell_value(i, 10),
                    str(datetime.datetime.now().date()),
                    str(uuid.uuid4()).replace('-',''),
                    str(datetime.datetime.utcfromtimestamp(seconds)),
                    # str(datetime.datetime.strptime(str(sheet.cell_value(i, 1)),'%d/%m/%Y %H:%i')),
                ))

                data_customer_list.append(str(sheet.cell_value(i, 4)).strip())
                data_customer["{}".format(str(sheet.cell_value(i, 4)).strip())] = {
                    'detail':{'full_name':str(sheet.cell_value(i, 4)).strip(),'date':sheet.cell_value(i, 1),'department_id':1,'is_active':1,},
                    'packs':[pack_data_item]
                }
            else:
                pass
                # try:
                #     data_customer["{}".format(str(sheet.cell_value(i, 4)).strip())]['packs'] = list(data_customer["{}".format(str(sheet.cell_value(i, 4)).strip())]['packs']).append(pack_data_item)
                # except:
                #     data_customer["{}".format(str(sheet.cell_value(i, 4)).strip())]['packs'] = [pack_data_item]
            # try:

            if_check_item = check_(str(sheet.cell_value(i, 4)).strip() , data_customer_list)
            # print("*************************------------*****************************")
            # print(str(sheet.cell_value(i, 4)).strip())
            # print(if_check_item)
            # print("*************************------------*****************************")
            azn_ids["{}".format(int(sheet.cell_value(i, 0)))] = {'real':int(sheet.cell_value(i, 0)),'exc':int(sheet.cell_value(i, 0))}

            packages_sql = "{}{}".format(packages_sql,"INSERT INTO `panel_package` VALUES ({},'{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}');".format(
                int(sheet.cell_value(i, 0)),
                sheet.cell_value(i, 3),
                str(datetime.datetime.utcfromtimestamp(seconds_first_date)),
                str(datetime.datetime.utcfromtimestamp(seconds_end_date))if seconds_end_date != 0 else 'NULL',
                """{}  {} {} {} """.format(
                    str(sheet.cell_value(i, 12)).strip(),
                    str(sheet.cell_value(i, 13)).strip(),
                    str(sheet.cell_value(i, 14)).strip(),
                    """{}{}""".format('komisiya haqq;: ',str(sheet.cell_value(i, 15)).strip(),) if str(sheet.cell_value(i, 15)).strip() else '',
                ),
                sheet.cell_value(i, 7),
                float(sheet.cell_value(i, 8)) * 100,
                sheet.cell_value(i, 7),
                status_bar["{}".format(sheet.cell_value(i, 9))],
                0,
                'NULL',
                str(datetime.datetime.utcfromtimestamp(seconds)),
                0,
                1,
                data_customer_list_dict["{}".format(if_check_item[1])],
                # len(data_customer_list) + 3,
                1,
                1,
                'NULL',
                'NULL',
                0,
                '',
                0.0,
            ))
            if sheet.cell_value(i, 10):
                numbers_id += 1
                numbers_sql = """{} INSERT INTO `panel_customerphonenumber`  VALUES ({},'{}',{}) """.format(
                    numbers_sql,
                    numbers_id,
                    """{}""".format(sheet.cell_value(i, 10)),
                    data_customer_list_dict["{}".format(if_check_item[1])],
                )
            if sheet.cell_value(i, 11):
                numbers_id += 1
                numbers_sql = """{} INSERT INTO `panel_customerphonenumber`  VALUES ({},'{}',{}) """.format(
                    numbers_sql,
                    numbers_id,
                    """{}""".format(sheet.cell_value(i, 11)),
                    data_customer_list_dict["{}".format(if_check_item[1])],
                )
            if sheet.cell_value(i, 12):
                numbers_id += 1
                numbers_sql = """{} INSERT INTO `panel_customerphonenumber`  VALUES ({},'{}',{}) """.format(
                    numbers_sql,
                    numbers_id,
                    """{}""".format(sheet.cell_value(i, 12)),
                    data_customer_list_dict["{}".format(if_check_item[1])],
                )
            if sheet.cell_value(i, 13):
                numbers_id += 1
                numbers_sql = """{} INSERT INTO `panel_customerphonenumber`  VALUES ({},'{}',{}) """.format(
                    numbers_sql,
                    numbers_id,
                    """{}""".format(sheet.cell_value(i, 13)),
                    data_customer_list_dict["{}".format(if_check_item[1])],
                )
            last_index = int(sheet.cell_value(i, 0))
        except:
            print("*************************------------*****************************")





        # except:
        #     pass
# print(data_custc
# omer_list[0])
# print(data_customer)
# print(data_customer_list)
# print(len(data_customer_list))
# print(data_customer_list_dict)
# data_customer_list

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(last_index)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

loc2 = ("l1-usd.xlsx")
wb_pack_usd = xlrd.open_workbook(loc2)
sheet_pack_usd = wb_pack_usd.sheet_by_index(0)
sheet_pack_usd.cell_value(0, 0)
for_i = 0


for i in range(sheet_pack_usd.nrows):
    for_i += 1
    if for_i > 2:
        try:
            # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            # print(sheet.cell_value(i, 1))
            # print(sheet.cell_value(i, 0))
            # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            serial_sate = float(sheet_pack_usd.cell_value(i, 1))
            seconds = (serial_sate - 25569) * 86400.0
            serial_first_date = float(sheet_pack_usd.cell_value(i, 5))
            seconds_first_date = (serial_first_date - 25569) * 86400.0
            try:
                serial_end_date = float(sheet_pack_usd.cell_value(i, 6))
                seconds_end_date = (serial_end_date - 25569) * 86400.0
            except:
                seconds_end_date = 0
            # print(datetime.datetime.utcfromtimestamp(seconds))
            # print(str(sheet_pack_usd.cell_value(i, 4)).strip()
            #       )
            # print(data_customer_list)

            if_check_item = check_(str(sheet_pack_usd.cell_value(i, 4)).strip() , data_customer_list)
            if if_check_item[0] == False:
                data_customer_list_dict["{}".format(str(sheet_pack_usd.cell_value(i, 4)).strip())] = len(data_customer_list)+3
                # print("--------------------------------------------------------------------------")
                # print(data_customer_list_dict["{}".format(str(sheet_pack_usd.cell_value(i, 4)).strip())])
                # print(str(sheet_pack_usd.cell_value(i, 4)).strip())
                # print("--------------------------------------------------------------------------")
                customer_sql = "{}{}".format(customer_sql,"INSERT INTO `panel_customer` VALUES({}, '{}', 'az12345678', '{}', '{}', '{}', '{}','{}', 1, '', '', '', '{}', 1, 'man');".format(
                    len(data_customer_list)+3,
                    str(sheet_pack_usd.cell_value(i, 4)).strip(),
                    'fin',
                    'address',
                    sheet_pack_usd.cell_value(i, 10),
                    str(datetime.datetime.now().date()),
                    str(uuid.uuid4()).replace('-',''),
                    str(datetime.datetime.utcfromtimestamp(seconds)),
                    # str(datetime.datetime.strptime(str(sheet_pack_usd.cell_value(i, 1)),'%d/%m/%Y %H:%i')),
                ))

                data_customer_list.append(str(sheet_pack_usd.cell_value(i, 4)).strip())
            else:
                pass
                # try:
                #     data_customer["{}".format(str(sheet_pack_usd.cell_value(i, 4)).strip())]['packs'] = list(data_customer["{}".format(str(sheet_pack_usd.cell_value(i, 4)).strip())]['packs']).append(pack_data_item)
                # except:
                #     data_customer["{}".format(str(sheet_pack_usd.cell_value(i, 4)).strip())]['packs'] = [pack_data_item]
            # try:

            if_check_item = check_(str(sheet_pack_usd.cell_value(i, 4)).strip() , data_customer_list)
            # print("*************************------------*****************************")
            # print(str(sheet_pack_usd.cell_value(i, 4)).strip())
            # print(if_check_item)
            # print("*************************------------*****************************")

            usd_ids["{}".format(int(sheet_pack_usd.cell_value(i, 0)))] = {'real':last_index + int(sheet_pack_usd.cell_value(i, 0)),'exc':int(sheet_pack_usd.cell_value(i, 0))}
            packages_sql = "{}{}".format(packages_sql,"INSERT INTO `panel_package` VALUES ({},'{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}');".format(
                last_index + int(sheet_pack_usd.cell_value(i, 0)),
                sheet_pack_usd.cell_value(i, 3),
                str(datetime.datetime.utcfromtimestamp(seconds_first_date)),
                str(datetime.datetime.utcfromtimestamp(seconds_end_date))if seconds_end_date != 0 else 'NULL',
                """{}  {} {} {} """.format(
                    str(sheet_pack_usd.cell_value(i, 12)).strip(),
                    str(sheet_pack_usd.cell_value(i, 13)).strip(),
                    str(sheet_pack_usd.cell_value(i, 14)).strip(),
                    """{}{}""".format('komisiya haqq;: ',str(sheet_pack_usd.cell_value(i, 15)).strip(),) if str(sheet_pack_usd.cell_value(i, 15)).strip() else '',
                ),
                sheet_pack_usd.cell_value(i, 7),
                float(sheet_pack_usd.cell_value(i, 8)) * 100,
                sheet_pack_usd.cell_value(i, 7),
                status_bar["{}".format(sheet_pack_usd.cell_value(i, 9))],
                0,
                'NULL',
                str(datetime.datetime.utcfromtimestamp(seconds)),
                0,
                2,
                data_customer_list_dict["{}".format(if_check_item[1])],
                # len(data_customer_list) + 3,
                1,
                1,
                'NULL',
                'NULL',
                0,
                '',
                0.0,
            ))
            if sheet_pack_usd.cell_value(i, 10):
                numbers_id += 1
                numbers_sql = """{} INSERT INTO `panel_customerphonenumber`  VALUES ({},'{}',{}) """.format(
                    numbers_sql,
                    numbers_id,
                    """{}""".format(sheet_pack_usd.cell_value(i, 10)),
                    data_customer_list_dict["{}".format(if_check_item[1])],
                )
            if sheet_pack_usd.cell_value(i, 11):
                numbers_id += 1
                numbers_sql = """{} INSERT INTO `panel_customerphonenumber`  VALUES ({},'{}',{}) """.format(
                    numbers_sql,
                    numbers_id,
                    """{}""".format(sheet_pack_usd.cell_value(i, 11)),
                    data_customer_list_dict["{}".format(if_check_item[1])],
                )
            if sheet_pack_usd.cell_value(i, 12):
                numbers_id += 1
                numbers_sql = """{} INSERT INTO `panel_customerphonenumber`  VALUES ({},'{}',{}) """.format(
                    numbers_sql,
                    numbers_id,
                    """{}""".format(sheet_pack_usd.cell_value(i, 12)),
                    data_customer_list_dict["{}".format(if_check_item[1])],
                )
            if sheet_pack_usd.cell_value(i, 13):
                numbers_id += 1
                numbers_sql = """{} INSERT INTO `panel_customerphonenumber` VALUES ({},'{}',{}) """.format(
                    numbers_sql,
                    numbers_id,
                    """{}""".format(sheet_pack_usd.cell_value(i, 13)),
                    data_customer_list_dict["{}".format(if_check_item[1])],
                )
        except:
            print("*************************------------*****************************")


        # except:
        #     pass



f= open("cus-1.sql","w+", encoding='utf8')
f2= open("pack-1.sql","w+", encoding='utf8')

f.write(customer_sql)
f.close()
f2.write(packages_sql)
f2.close()

print(len(usd_ids.items()))




f= open("cus-1.sql","w+", encoding='utf8')
f3= open("cus-1-phone.sql","w+", encoding='utf8')
f2= open("pack-1.sql","w+", encoding='utf8')

f.write(customer_sql)
f.close()
f3.write(numbers_sql)
f3.close()
f2.write(packages_sql)
f2.close()





pay_usd = ("l1p-usd.xlsx")
pay_azn = ("l1p-azn.xlsx")
wb_usd = xlrd.open_workbook(pay_usd)
sheet_usd = wb_usd.sheet_by_index(0)
sheet_usd.cell_value(0, 0)

wb_azn = xlrd.open_workbook(pay_azn)
sheet_azn = wb_azn.sheet_by_index(0)
sheet_azn.cell_value(0, 0)


pay_azn_sql = ''
pay_usd_sql = ''

all_payments_i = 0
for_i = 0
for i in range(sheet_azn.nrows):
    for_i += 1
    if for_i > 2:
        # try:
        all_payments_i += 1
        try:
            serial_pay = float(sheet_azn.cell_value(i, 2))
            seconds = (serial_pay - 25569) * 86400.0
        except:
            seconds = 0
        # print(datetime.datetime.utcfromtimestamp(seconds))
        # print(str(sheet_azn.cell_value(i, 4)).strip()
        #       )
        # print(data_customer_list)
        difer = 0
        if sheet_azn.cell_value(i, 4) and sheet_azn.cell_value(i, 5):
            try:
                difer = round(float(sheet_azn.cell_value(i, 4)) - float(sheet_azn.cell_value(i, 5)),2)
            except:
                print("-----------------------------###################################################")
                print(sheet_azn.cell_value(i, 5))
                print("-----------------------------###################################################")
        else:
            if sheet_azn.cell_value(i, 4):
                difer = round(sheet_azn.cell_value(i, 4),2)
            elif sheet_azn.cell_value(i, 5):
                difer = round(sheet_azn.cell_value(i, 5),2)
        pay_azn_sql = "{}{}".format(pay_azn_sql,"INSERT INTO `panel_packagepaymentdates` VALUES ({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(
            all_payments_i,
            """{}""".format(sheet_azn.cell_value(i, 8) if sheet_azn.cell_value(i, 8) else 0),
            str(datetime.datetime.utcfromtimestamp(seconds)),
            str(datetime.datetime.utcfromtimestamp(seconds)),
            sheet_azn.cell_value(i, 6) if sheet_azn.cell_value(i, 6) else 0,
            0,
            float(sheet_azn.cell_value(i, 3)) if sheet_azn.cell_value(i, 3) else 0,
            """{}""".format(sheet_azn.cell_value(i, 4) if sheet_azn.cell_value(i, 4) and str(sheet_azn.cell_value(i, 4)).strip() != '' else 0),
            """{}""".format(sheet_azn.cell_value(i, 5) if sheet_azn.cell_value(i, 5) and str(sheet_azn.cell_value(i, 5)).strip() != '' else 0),
            difer,
            """{}""".format(str(sheet_azn.cell_value(i, 7)).strip().replace('\'','').replace('\\','')),
            str(datetime.datetime.utcfromtimestamp(seconds)),
            azn_ids["{}".format(int(sheet_azn.cell_value(i, 1)))]['real'],
            1,
            float(sheet_azn.cell_value(i, 9)) if sheet_azn.cell_value(i, 9) else 0,
        ))
        # except:
        #     print("*************************------------*****************************")


        # except:
        #     pass



fp1= open("pay-azn.sql","w+", encoding='utf8')
fp1.write(pay_azn_sql)
fp1.close()





print("--------------------------------------------")
print(all_payments_i)
print("--------------------------------------------")



for_i = 0
for i in range(sheet_usd.nrows):
    for_i += 1
    if for_i > 2:
        try:
            all_payments_i += 1
            try:
                serial_pay = float(sheet_usd.cell_value(i, 2))
                seconds = (serial_pay - 25569) * 86400.0
            except:
                seconds = 0
            # print(datetime.datetime.utcfromtimestamp(seconds))
            # print(str(sheet_usd.cell_value(i, 4)).strip()
            #       )
            # print(data_customer_list)
            difer = 0
            if sheet_usd.cell_value(i, 4) and sheet_usd.cell_value(i, 5):
                try:
                    difer = round(float(sheet_usd.cell_value(i, 4)) - float(sheet_usd.cell_value(i, 5)),2)
                except:
                    print("-----------------------------###################################################")
                    print(sheet_usd.cell_value(i, 5))
                    print("-----------------------------###################################################")
            else:
                if sheet_usd.cell_value(i, 4):
                    difer = sheet_usd.cell_value(i, 4)
                elif sheet_usd.cell_value(i, 5):
                    difer = sheet_usd.cell_value(i, 5)
            pay_usd_sql = "{}{}".format(pay_usd_sql,"INSERT INTO `panel_packagepaymentdates` VALUES ({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(
                all_payments_i,
            """{}""".format(sheet_usd.cell_value(i, 8) if sheet_usd.cell_value(i, 8) and str(sheet_usd.cell_value(i, 8)).strip() != '' else 0),
                str(datetime.datetime.utcfromtimestamp(seconds)),
                str(datetime.datetime.utcfromtimestamp(seconds)),
                sheet_usd.cell_value(i, 6) if sheet_usd.cell_value(i, 6) else 0,
                0,
                float(sheet_usd.cell_value(i, 3)) if sheet_usd.cell_value(i, 3) else 0,
                """{}""".format(sheet_usd.cell_value(i, 4) if sheet_usd.cell_value(i, 4) and str(sheet_usd.cell_value(i, 4)).strip() != '' else 0),
                """{}""".format(sheet_usd.cell_value(i, 5) if sheet_usd.cell_value(i, 5) and str(sheet_usd.cell_value(i, 5)).strip() != '' else 0),
                difer,
                """{}""".format(str(sheet_usd.cell_value(i, 7)).strip().replace('\'','').replace('\\','')),
                str(datetime.datetime.utcfromtimestamp(seconds)),
                usd_ids["{}".format(int(sheet_usd.cell_value(i, 1)))]['real'],
                1,
                float(sheet_usd.cell_value(i, 9)) if sheet_usd.cell_value(i, 9) else 0,
            ))
        except:
            print("*************************------{}------*****************************".format(sheet_usd.cell_value(i, 0)))


        # except:
        #     pass



fp2= open("pay-usd.sql","w+", encoding='utf8')

fp2.write(pay_usd_sql)
fp2.close()
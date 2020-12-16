from django.conf.urls import url

from .views import *


urlpatterns = [
	url(r'^$', dashboard, name='dashboard'),
	# url(r'^video-posts/list/$', video_posts, name='video-posts'),
	# url(r'^customers/list/$', customer_list, name='customer-list'),
	url(r'^customers/list/(?P<type>[\w-]+)/$', customer_list_type, name='customer-list-type'),
	url(r'^customers/list/m/ajax/$', customer_list_ajax, name='customer-ajax-list'),
	url(r'^customers/create/$', add_customer, name='customer-create'),
	url(r'^customers/edit/(?P<id>[0-9]+)/$', edit_customer, name='customer-edit'),

	url(r'^packages/annuitet/(?P<id>[0-9]+)/$', package_annuitet, name='package-annuitet'),
	url(r'^packages-an/annuitet-general/$', general_annuitet, name='general-annuitet'),
	url(r'^packages-an/upload_base64/$', upload_base64, name='upload_base64'),


	url(r'^statistic/(?P<type>[\w-]+)/$', statistic_type, name='statistic-type'),




	url(r'^packages/list/$', package_list, name='package-list'),
	url(r'^packages/list/(?P<type>[\w-]+)/$', package_list_type, name='package-list-type'),
	url(r'^packages/list/infinity/(?P<type>[\w-]+)/$', package_list_type_infinity, name='package-list-type-infinity'),
	url(r'^packages/package-daily-note-write/(?P<id>[0-9]+)/$', package_daily_note_ajax, name='package-daily-note'),
	url(r'^packages/package-daily-note-list/(?P<id>[0-9]+)/$', package_daily_note_list, name='package-daily-list'),
	url(r'^product-type/get-ajax/$', product_type_ajax, name='product-type-ajax'),
	url(r'^packages/closed-reason/(?P<id>[0-9]+)/$', package_closed_reason, name='package-closed-reason'),
	url(r'^packages/waiting/list/(?P<type>[\w-]+)/$', package_waiting_list, name='package-waiting-list'),
	url(r'^packages/waiting/edit/(?P<id>[0-9]+)/$', package_waiting_edit, name='package-waiting-edit'),
	url(r'^packages/waiting/list/(?P<p_id>[0-9]+)/(?P<type>[\w-]+)/$', package_waiting_list_package, name='package-waiting-list-package'),

	url(r'^packages/create/$', package_create, name='package-create'),
	url(r'^packages/edit/(?P<id>[0-9]+)/$', package_edit, name='package-edit'),
	url(r'^package-atachment-upload/(?P<id>[0-9]+)/ajax/$', package_atachment_upload, name='package-atachment-upload'),



	url(r'^packages/payments-edit/(?P<id>[0-9]+)/$', package_payment_edit, name='package-payments-edit'),
	url(r'^packages/payments-refresh/(?P<id>[0-9]+)/$', package_payment_refresh, name='package-payments-refresh'),
	url(r'^packages/payments-remove/(?P<id>[0-9]+)/$', package_payment_remove, name='package-payments-remove'),
	url(r'^packages/payments-new-generate/(?P<id>[0-9]+)/$', package_payment_new_generate, name='package-payments-new-generate'),
	url(r'^packages/payment-new-check/(?P<id>[0-9]+)/$', package_payment_new_check, name='package-payment-new-check'),
	url(r'^packages/payment-new-add/(?P<id>[0-9]+)/$', package_payment_new_add, name='package-payment-new-add'),
	url(r'^packages/payment-ajax/(?P<id>[0-9]+)/$', package_payment_add, name='package-add-paymanet'),

	url(r'^packages/ordered/list/$', package_ordered_list, name='package-ordered-list'),
	url(r'^packages/next/(?P<o_slug>[\w-]+)/(?P<id>[0-9]+)/$', package_next, name='package-next'),
	url(r'^packages/ordered/edit/(?P<id>[0-9]+)/$', package_ordered_edit, name='package-ordered-edit'),

    url(r'^salaries/list/$', salary_list, name='salary-list'),
	url(r'^employees/list/$', employee_list, name='employee-list'),
	url(r'^employees/create/$', employee_create, name='employee-create'),
	url(r'^employees/edit/(?P<id>[0-9]+)/$', employee_edit, name='employee-edit'),

	url(r'^employees-permit/list/$', employee_permit_list, name='employee-permit-list'),
	url(r'^employees-permit/create/$', employee_permit_create, name='employee-permit-create'),
	url(r'^employees-permit/edit/(?P<id>[0-9]+)/$', employee_permit_edit, name='employee-permit-edit'),

	url(r'^reports/logs/list/$', log_list, name='log-list'),
	url(r'^reports/logs/outcome/ajax/$', logo_outcome_data_ajax, name='logo-outcome-ajax-data-list'),
	url(r'^reports/logs/detail/(?P<id>[0-9]+)/$', log_detail, name='log-detail'),
	url(r'^reports/(?P<o_slug>[\w-]+)/list/$', income_outcome_list, name='income-outcome-list'),
	url(r'^reports/list/kassa/$', income_outcome_case, name='income-outcome-case'),
	url(r'^reports/list/kassa/$', income_outcome_case, name='income-outcome-case'),
	url(r'^reports/(?P<o_slug>[\w-]+)/create/$', income_outcome_create, name='income-outcome-create'),
	url(r'^reports/(?P<o_slug>[\w-]+)/edit/(?P<id>[0-9]+)/$', income_outcome_edit, name='income-outcome-edit'),


	url(r'^currency/list/$', currency_list, name='currency-list'),
	url(r'^currency/create/$', currency_create, name='currency-create'),
	url(r'^currency/edit/(?P<id>[0-9]+)/$', currency_edit, name='currency-edit'),

	url(r'^customer-notes/list/(?P<c_id>[0-9]+)/$', customer_notes_list, name='customer-notes-list'),
	url(r'^customer-notes/create/(?P<c_id>[0-9]+)/$', customer_notes_create, name='customer-notes-create'),
	url(r'^customer-notes/edit/(?P<c_id>[0-9]+)/(?P<id>[0-9]+)/$', customer_notes_edit, name='customer-notes-edit'),

	url(r'^departments/list/', department_list, name='department-list'),
	url(r'^departments/create/', department_create, name='department-create'),
	url(r'^departments/edit/(?P<id>[0-9]+)/', department_edit, name='department-edit'),

	url(r'^package-types/list/', package_type_list, name='package_type-list'),
	url(r'^package-types/create/', package_type_create, name='package_type-create'),
	url(r'^package-types/edit/(?P<id>[0-9]+)/', package_type_edit, name='package_type-edit'),
	url(r'^package-types/remove/(?P<id>[0-9]+)/', package_type_remove, name='package_type-remove'),

	url(r'^product/list/', product_list, name='product-list'),
	url(r'^product/create/', product_create, name='product-create'),
	url(r'^product/edit/(?P<id>[0-9]+)/', product_edit, name='product-edit'),
	url(r'^product/remove/(?P<id>[0-9]+)/', product_remove, name='product-remove'),

	url(r'^product-type/generate/', product_generate, name='product-type-generate-ajax'),
	url(r'^product-type/list/(?P<p_id>[0-9]+)/', product_type_list, name='product-type-list'),
	url(r'^product-type/create/(?P<p_id>[0-9]+)/', product_type_create, name='product-type-create'),
	url(r'^product-type/edit/(?P<p_id>[0-9]+)/(?P<id>[0-9]+)/', product_type_edit, name='product-type-edit'),
	url(r'^product-type/remove/(?P<p_id>[0-9]+)/(?P<id>[0-9]+)/', product_type_remove, name='product-type-remove'),

	url(r'^package-product/remove/(?P<id>[0-9]+)/', package_product_remove, name='package-product-image-remove'),


 ]
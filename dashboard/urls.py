from django.conf.urls import url

from . import views

urlpatterns=[
url(r'^$', views.index ,name='index'),
url(r'^display_cashiers/', views.display_cashiers, name='display_cashiers'),
        url(r'^add_staff/', views.add_staff, name='add_staff'),
url(r'^display_viewstaff/', views.display_viewstaff, name='display_viewstaff'),

url(r'^enter_expenditure/', views.enter_expenditure, name='enter_expenditure'),
url(r'^enter_sundryexpense', views.enter_sundryexpense ,name='enter_sundryexpense'),
url(r'^pay_salary/', views.pay_salary, name='pay_salary'),

url(r'^sundryreport', views.sundryreport ,name='sundryreport'),
url(r'^salaryreport/', views.salaryreport, name='salaryreport'),
url(r'^expenditurereport/', views.expenditurereport, name='expenditurereport'),


url(r'^salariespdf/', views.salariespdf.as_view() ,name='salariespdf'),
url(r'^sundrypdf/', views.sundrypdf.as_view() ,name='sundrypdf'),
url(r'^expenditurepdf/', views.expenditurepdf.as_view() ,name='expenditurepdf'),

url(r'^expensereceipt/', views.expensereceipt.as_view() ,name='expensereceipt'),
url(r'^salaryreceipt/', views.salaryreceipt.as_view() ,name='salaryreceipt'),
url(r'^sundryreceipt/', views.sundryreceipt.as_view() ,name='sundryreceipt'),

        url(r'^expenditurearchive/', views.expenditurearchive, name='expenditurearchive'),
        url(r'^salaryarchive/', views.salaryarchive, name='salaryarchive'),
        url(r'^sundryarchive/', views.sundryarchive, name='sundryarchive'),

        url(r'^expenditurearchivepdf/', views.expenditurearchivepdf, name='expenditurearchivepdf'),
        url(r'^salaryarchivepdf/', views.salaryarchivepdf, name='salaryarchivepdf'),
        url(r'^sundryarchivepdf/', views.sundryarchivepdf, name='sundryarchivepdf'),
        ]
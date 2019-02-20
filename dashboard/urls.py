from django.conf.urls import url
from .import views

urlpatterns=[
url(r'^$', views.index ,name='index'),
url(r'^display_cashiers/', views.display_cashiers, name='display_cashiers'),
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
    ]
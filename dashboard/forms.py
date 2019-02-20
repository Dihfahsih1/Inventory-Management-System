from django import forms
from .models import *


class SpendForm(forms.ModelForm):
    class Meta:
        model=Spend
        fields=('Date','PaymentMadeTo','ReasonForPayment','Amount', 'ReceivedBy', 'ApprovedBy')

class SundryForm(forms.ModelForm):
    class Meta:
        model=Sundry
        fields=('Date','PaymentMadeTo','Amount','ReasonForPayment')

class SalaryForm(forms.ModelForm):
    class Meta:
        model=Salary
        fields = ('Date','Amount','Staff','Salary_Type','Month')

class StaffDetailsForm(forms.ModelForm):
    class Meta:
        model=StaffDetails
        fields=('FistName','SecondName','Salary','Role','Duties','Sex','Contact')




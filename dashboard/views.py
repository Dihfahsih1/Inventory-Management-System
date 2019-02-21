#views
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import View
from .render import Render

from .forms import *
from .models import *
from django.db.models import Sum


def index(request):
    return render(request,'Accprofile.html')

def display_cashiers(request):
    return render(request, 'Accprofile.html')

    ####################################################
    #        ENTERING RECORDS INTO THE DATABASE        #
    ####################################################

 # payment of salaries
def pay_salary(request):
    if request.method=="POST":
        form=SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salaryreceipt')
    else:
        form=SalaryForm()
        return render(request, 'add_new.html',{'form':form})


# recording the major expenditures
def enter_expenditure(request):
    if request.method=="POST":
        form=SpendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('expensereceipt')
    else:
        form=SpendForm()
        return render(request, 'add_new.html',{'form':form})

  #recording small expenses
def enter_sundryexpense(request):
    if request.method=="POST":
        form=SundryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('sundryreceipt')
    else:
        form=SundryForm()
        return render(request, 'add_new.html',{'form':form})


        ####################################################
        #                VIEWING  THE REPORTS              #
        ####################################################

def display_viewstaff(request):
    all_staff = StaffDetails.objects.all()
    return render(request,'index.html',{'Staffs': all_staff})

       ####################################################
      #        CALCULATING TOTALS IN THE REPORTS         #
      ####################################################

    # calculating totals in salary Report
def salaryreport (request):
  queryset = Salary.objects.all().order_by('-Date')
  total = 0
  for instance in queryset:
      total+=instance.Amount
  context = {
      'queryset':queryset,
      'total': total,
  }
  return render(request, 'salaryindex.html', context)

#def expenditurereport(request):
def expenditurereport (request):
  queryset = Spend.objects.all().order_by('-Date')
  total = 0
  for instance in queryset:
      total+=instance.Amount
  context = {
      'queryset':queryset,
      'total': total,
  }
  return render(request, 'expenditureindex.html', context)

#calculating totals in sundryexpense report
def sundryreport (request):
  queryset = Sundry.objects.all().order_by('-Date')
  total = 0
  for instance in queryset:
      total+=instance.Amount
  context = {
      'queryset':queryset,
      'total': total,
  }
  return render(request, 'sundryindex.html', context)



       ####################################################
      #        GENERATING REPORTS IN FORM OF PDFS         #
      ####################################################

#Printing Expenditure Report
class expenditurepdf(View):
    def get(self, request):
        expense = Spend.objects.all().order_by('-Date')
        today = timezone.now()
        totalexpense = 0
        for instance in expense:
            totalexpense += instance.Amount
        expensecontext ={
            'today':today,
            'expense':expense,
            'request': request,
            'totalexpense': totalexpense,
        }
        return Render.render('expenditurepdf.html',expensecontext)

#Printing Salaries Report
class salariespdf(View):
    def get(self, request):
        salaries = Salary.objects.all().order_by('-Date')
        today = timezone.now()
        totalsalary = 0
        for instance in salaries:
            totalsalary += instance.Amount
        salarycontext ={
            'today':today,
            'salaries':salaries,
            'request': request,
            'totalsalary': totalsalary,
        }
        return Render.render('pdf.html',salarycontext)



#Printing Sundry Expenses Report
class sundrypdf(View):
    def get(self, request):
        sundry = Sundry.objects.all().order_by('-Date')
        today = timezone.now()
        totalsundry = 0
        for instance in sundry:
            totalsundry += instance.Amount
        sundrycontext ={
            'today':today,
            'sundry':sundry,
            'request': request,
            'totalsundry': totalsundry,
        }
        return Render.render('sundrypdf.html',sundrycontext)


        ####################################################
        #        ARCHIVING OF THE MONTHLY REPORTS          #
        ####################################################




        ####################################################
        #       PRINTING THE RECEIPTS                      #
        ####################################################

class expensereceipt(View):
    def get(self, request):
        expense = Spend.objects.all().filter().last()
        today = timezone.now()
        expensecontext = {
            'today': today,
            'expense': expense,
            'request': request,
        }
        return Render.render('expensereceipt.html', expensecontext)

class salaryreceipt(View):
    def get(self, request):
        salary= Salary.objects.all().filter().last()
        today = timezone.now()
        salarycontext = {
            'today': today,
            'salary': salary,
            'request': request,
        }
        return Render.render('salaryreceipt.html', salarycontext)

class sundryreceipt(View):
    def get(self, request):
        sundry = Sundry.objects.all().filter().last()
        today = timezone.now()
        sundrycontext = {
            'today': today,
            'sundry': sundry,
            'request': request,
        }
        return Render.render('sundryreceipt.html', sundrycontext)



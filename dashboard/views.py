#views
from datetime import datetime

from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View

from .forms import *
from .models import *
from .render import Render


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
    current_month = datetime.now().month
    queryset = Salary.objects.all().filter(Date__month=current_month).order_by('-Date')
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
    current_month = datetime.now().month
    queryset = Spend.objects.all().filter(Date__month=current_month).order_by('-Date')
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
    current_month = datetime.now().month
    queryset = Sundry.objects.filter(Date__month=current_month).order_by('-Date')
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
        current_month = datetime.now().month
        expense = Spend.objects.filter(Date__month=current_month).order_by('-Date')

        today = timezone.now()
        month = today.strftime('%B')
        totalexpense = 0
        for instance in expense:
            totalexpense += instance.Amount
        expensecontext ={

            'month': month,
            'today':today,
            'expense':expense,
            'request': request,
            'totalexpense': totalexpense,
        }
        return Render.render('expenditurepdf.html',expensecontext)

#Printing Salaries Report
class salariespdf(View):
    def get(self, request):
        current_month = datetime.now().month
        salaries = Salary.objects.filter(Date__month=current_month).order_by('-Date')
        today = timezone.now()
        month = today.strftime('%B')
        totalsalary = 0
        for instance in salaries:
            totalsalary += instance.Amount
        salarycontext ={
            'month': month,
            'today':today,
            'salaries':salaries,
            'request': request,
            'totalsalary': totalsalary,
        }
        return Render.render('pdf.html',salarycontext)

#Printing Sundry Expenses Report
class sundrypdf(View):
    def get(self, request):
        current_month = datetime.now().month
        sundry = Sundry.objects.filter(Date__month=current_month).order_by('-Date')
        today = timezone.now()
        month = today.strftime('%B')
        totalsundry = 0
        for instance in sundry:
            totalsundry += instance.Amount
        sundrycontext ={
            ''
            'month': month,
            'today':today,
            'sundry':sundry,
            'request': request,
            'totalsundry': totalsundry,
        }
        return Render.render('sundrypdf.html',sundrycontext)




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


        ####################################################
        #        ARCHIVING OF THE MONTHLY REPORTS          #
        ####################################################


def salaryarchive(request):
    queryset = Salary.objects.all().order_by('-Date')
    total = 0
    for instance in queryset:
        total += instance.Amount
    context = {
        'queryset': queryset,
        'total': total,
    }
    return render(request, 'salaryarchive.html', context)


# def expenditurereport(request):
def expenditurearchive(request):
    queryset = Spend.objects.all().order_by('-Date')
    total = 0
    for instance in queryset:
        total += instance.Amount
    context = {
        'queryset': queryset,
        'total': total,
    }
    return render(request, 'expenditurearchive.html', context)


# calculating totals in sundryexpense report
def sundryarchive(request):
    queryset = Sundry.objects.all().order_by('-Date')
    total = 0
    for instance in queryset:
        total += instance.Amount
    context = {
        'queryset': queryset,
        'total': total,
    }
    return render(request, 'sundryarchive.html', context)

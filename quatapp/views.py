from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse, HttpResponse
# from .forms import ContactForm,UserCreationForm,CreateUserForm
from .models import Profits
# from ajax_datatable import AjaxDatatableView
# from django.urls import reverse
# from django.forms import model_to_dict
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user,allowed_user
from django.contrib.auth.models import User
from django.views.generic import TemplateView, View, DeleteView
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import datetime
from django.db.models import Sum

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request,username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print("Logined success")
            return redirect('home')
        else:
            messages.info(request,"Username or Password is Incorrect!")
            return render(request,"login.html")
    return render(request,"login.html")

def logout(request):
    auth_logout(request)
    return redirect('home')

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken")
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)

        messages.success(request, "Account was created successfully")
        return redirect('login')
    return render(request, "register.html")



def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"home.html")

def our_services(request):
    return render(request,"our_services.html")

def profit_details(request):
    return render(request,"profit_details.html")

def ai_robot(request):
    profits = Profits.objects.all().order_by('-id')  
    weekly_profits = get_weekly_profits()
    monthly_profits = get_monthly_profits()
    return render(request, "ai_robot.html", {'profits': profits, 'weekly_profits': weekly_profits, 'monthly_profits': monthly_profits})



def contact(request):
    return render(request,"contact.html")



from django.db.models import Sum
from django.db.models.functions import ExtractWeek, ExtractMonth

def get_weekly_profits():
    # Calculate the start and end date for the current week
    today = datetime.date.today()
    start_of_week = today - datetime.timedelta(days=today.weekday())
    end_of_week = start_of_week + datetime.timedelta(days=6)

    # Query the database for profits within the current week and aggregate USD and INR values
    weekly_profits = Profits.objects.filter(date__range=[start_of_week, end_of_week]).aggregate(
        total_usd=Sum('usd'),
        total_inr=Sum('inr')
    )

    return {'start_date': start_of_week, 'end_date': end_of_week, 'total_usd': weekly_profits['total_usd'], 'total_inr': weekly_profits['total_inr']}


def get_monthly_profits():
    # Calculate the start and end date for the current month
    today = datetime.date.today()
    start_of_month = today.replace(day=1)
    end_of_month = today.replace(day=1) + datetime.timedelta(days=32)

    # Query the database for profits within the current month and aggregate USD and INR values
    monthly_profits = Profits.objects.filter(date__range=[start_of_month, end_of_month]).annotate(
        month=ExtractMonth('date')
    ).values('month').annotate(
        total_usd=Sum('usd'),
        total_inr=Sum('inr')
    )

    return monthly_profits


# class ProfitView(TemplateView):
#     template_name = 'ai_robot.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['users'] = Profits.objects.all()
#         return context
    
# @csrf_exempt
class CreateProfit(View):
    def post(self, request):
        date = request.POST.get('date', None)
        usd = request.POST.get('usd', None)
        inr = request.POST.get('inr', None)
        result = request.POST.get('result', None)

        obj = Profits.objects.create(
            date=date,
            usd=usd,
            inr=inr,
            result=result,
        )

        user = {'id': obj.id, 'date': obj.date, 'usd': obj.usd, 'inr': obj.inr, 'result': obj.result}

        data = {
            'profit': user
        }
        return JsonResponse(data)

# @csrf_exempt
class DeleteProfit(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        Profits.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

# @csrf_exempt
class UpdateProfit(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        date = request.POST.get('date', None)
        usd = request.POST.get('usd', None)
        inr = request.POST.get('inr', None)
        result = request.POST.get('result', None)

        obj = Profits.objects.get(id=id1)
        obj.date = date
        obj.usd = usd
        obj.inr = inr
        obj.result = result
        obj.save()

        user = {'id': obj.id, 'date': obj.date, 'usd': obj.usd, 'inr': obj.inr, 'result': obj.result}

        data = {
            'profit': user
        }
        return JsonResponse(data)
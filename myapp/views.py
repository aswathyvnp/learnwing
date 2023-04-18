
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from .forms import OtherModelForm
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from myapp.models import Addcart, OtherModel
from django.contrib import messages
from LearnwingApp.models import SubCourse,Course,Course_Category
from django.urls import reverse
from django.contrib.auth.models import User
import uuid



# from myapp.models import Mmodel

from django.http import HttpResponseBadRequest

import razorpay
import json
from django.views.decorators.csrf import csrf_exempt

from flask import Flask,request
# Create your views here.
# def Home(request):
#     return render(request,"app.html")

app = Flask(__name__,static_folder = "static", static_url_path='')
razorpay_client = razorpay.Client(auth=("rzp_test_acgCaQhDp1w1uK", "8egrozmgdp1GGzZ2DYvNNRcl"))

def app_create(request):
    return render(request,"app.html")

@csrf_exempt
def app_charge(request,id):
    object = SubCourse.objects.get(id=id)
    # amount = object.course_fee
    return render(request, "successpage.html",{'object':object})
if __name__ == '__main__':
    app.run()


# Create your views here.
def register(request):
    
    form=CreateUserForm(request.POST)
    form1=OtherModelForm(request.POST,request.FILES)
    if form.is_valid() and form1.is_valid():
        user = form.save()
        customer =form1.save(commit=False)
        customer.user = user
        customer.save()
        return redirect('/loginpage')
    else:
        form = CreateUserForm()
        form1 = OtherModelForm()
    return render(request,'register.html',{'form':form,'form1':form1})


def searchitem(request):
    # imageSearch=SubCourse.objects.all()
    if request.method == 'GET':
        query=request.GET.get('search')
        if query == '':
            query = 'None'
        results=SubCourse.objects.filter(course_title__icontains=query)
    return render(request,'index.html',{'results': results})


def Loginpage(request):
    course = SubCourse.objects.all()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_staff and user.is_superuser:
                login(request, user)
                return redirect('/adminpage')
            elif user.is_staff:
                login(request, user)
                return redirect('/dashboard')
            else:
            #  messages.success(request,'Wrong Password')
                login(request,user)
                return redirect('/dashboard')
    return render(request,'loginpage.html',{'course':course})
    # return render(request,'index.html')


def Course(request,id):
    object=SubCourse.objects.get(id=id)
    # object1=SubCourse.objects.get(user=id)
    course = SubCourse.objects.all()
    return render(request,'course.html',{'obj':object,'course':course})


@login_required(login_url='/login')
def DashboardPage(request):
    object1=OtherModel.objects.get(user=request.user)
    course = SubCourse.objects.all()
    # return render(request,'index.html',{'course':course})
    return render(request,'dashboard.html',{'user':object1,'course':course})


def logoutPage(request):
    logout(request)
    return redirect('index')

def Home(request):
    course = SubCourse.objects.all()  
    return render(request,'index.html',{'course':course})

# @login_required(login_url='/loginpage2' ,redirect_field_name=None)
# @login_required(login_url='/loginpage2')

def payment1(request, id):
    if request.user.is_authenticated:
        try:
            object1 = OtherModel.objects.get(user=request.user)
        except OtherModel.DoesNotExist:
            object1 = None
        object = SubCourse.objects.get(id=id)
        course = SubCourse.objects.all()
        return render(request, 'payment.html', {'obj': object, 'course': course, 'user': object1})
    else:
        request.session['id'] = id
        login_url = reverse('loginpage2')
        return redirect(login_url)


# def payment1(request, id):
#     if request.user.is_authenticated:
#         object1 = OtherModel.objects.get(user=request.user)
#         object = SubCourse.objects.get(id=id)
#         course = SubCourse.objects.all()
#         return render(request, 'payment.html', {'obj': object, 'course': course, 'user': object1})
#     else:
#         request.session['id'] = id
#         login_url = reverse('loginpage2')
#         return redirect(login_url)

# def payment1(request,id):
#     object1=OtherModel.objects.get(user=request.user)
#     object=SubCourse.objects.get(id=id)
#     # object1=SubCourse.objects.get(user=id)
#     course = SubCourse.objects.all()
#     if request.user.is_authenticated:
#         return render(request,'payment.html',{'obj':object,'course':course,'user':object1})
#     else:
#         request.session['id']=id
#         login_url=reverse('loginpage2')
#         return redirect(login_url)


def Loginpage2(request):
    id=request.session.get('id')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            messages.success(request,'Wrong Password')
            login(request,user)
            return redirect('payment1',id=id)
    return render(request,'loginpage.html')
    # return render(request,'index.html')

# def Bill(request,id):
#     object=SubCourse.objects.get(id=id)    
#     return render(request,'bill.html',{'obj':object})

def Bill(request, id):
    object = SubCourse.objects.get(id=id)
    bill_id = str(uuid.uuid4())  # generate a random bill ID
    return render(request, 'bill.html', {'obj': object, 'bill_id': bill_id})

def generate_bill_id():
    return str(uuid.uuid4())


# def AddCart(request):
    
#     return render(request,'addcart.html')


def Addtocart(request,id):
    uid=request.user
    obj=Addcart.objects.get(u_id=id)
    Main_course = SubCourse.objects.get(id=id)
    c = Addcart(u_id=uid, course_id=Main_course)
    c.save()
    return render(request,'addcart.html',{'data':obj})
    
    

def ViewCart(request,id):
    obj=Addcart.objects.get(u_id=id)
    return render(request,{'data':obj})

def generate_bill_id():
    return str(uuid.uuid4())


# def add_to_cart(request, id):
#     product = SubCourse.objects.get(id=id)
#     cart = Cart(request)
#     cart.add(product, product.course_fee)

# def remove_from_cart(request,id):
#     product = SubCourse.objects.get(id=id)
#     cart = Cart(request)
#     cart.remove(product)

# def get_cart(request):
#     return render(request, 'cart.html', {'cart': Cart(request)})
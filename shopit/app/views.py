
# Create your views here.

from django.shortcuts import render
from django.views import View
from .models import*
from .forms import *
from django.http import request , response 
from django.contrib import messages
from .forms import CustomerRegistrationForm , CustomerProfileForm




#def home(request):
# return render(request, 'app/home.html')


class ProductView(View):
    def get(self , request):
        
        #here we will get the products that are 
        topwears = Product.objects.filter(category = 'TW')
        bottompwears = Product.objects.filter(category = 'BW')
        mobiles = Product.objects.filter(category = 'M')                        #passing our dictionsary into the context
        return render(request , 'app/home.html' , {'topwears': topwears , 'bottomwears' : bottompwears , 'mobiles': mobiles})


class ProductDEtailView(View):
    def get(self , request , pk):
        product = Product.objects.get(pk = pk)
        return render(request , 'app/productdetail.html' , {'product' : product})




def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request , data = None):
    brands = ['Apple' , 'Samsung' , 'Redmi' , 'Realmi' , 'Nokia' , 'Oneplus' , 'Oppe' , 'Vivo' , 'Lenovo' , 'Asus' , 'RedMagic' , 'Razor' , 'Pixel' ]
    if data == None:
        mobiles = Product.objects.filter(category = 'M')  #show all phones
    elif data == 'below':
        mobiles = Product.objects.filter(category = 'M').filter(discounted_price__lt =20000)
    elif data == 'above':
        mobiles = Product.objects.filter(category = 'M').filter(discounted_price__gt =20000)
    else:
        mobiles = Product.objects.filter(category = 'M').filter(brand = data)
        
    return render(request, 'app/mobile.html' , {'mobiles': mobiles , 'brands' : brands})



#def customerregistration(request):
 #return render(request, 'app/customerregistration.html')
class CustomerRegistrationView(View):
    def get(self , request):
        form = CustomerRegistrationForm
        return render(request , 'app/customerregistration.html' , {'form' : form})  
        
    def post(self , request):
        
        form  = CustomerRegistrationForm(request.POST)
        
        if form.is_valid():
            messages.success(request , 'Successfully registered!')
            form.save()
        return render(request , 'app/customerregistration.html' , {'form' : form})   


class ProfileView(View):
    def get(self , request):
        form = CustomerProfileForm()
        return render(request , 'app/profile.html' , {'form':form})
       




def checkout(request):
 return render(request, 'app/checkout.html')



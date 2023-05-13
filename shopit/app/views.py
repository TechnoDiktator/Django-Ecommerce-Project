
# Create your views here.

from django.shortcuts import render,redirect
from django.views import View
from .models import*
from .forms import *
from django.http import request , response 
from django.contrib import messages
from .forms import CustomerRegistrationForm , CustomerProfileForm
from django.db.models import Q
from django.http import JsonResponse




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
    user = request.user
    productid = request.GET.get('prod_id')
    product = Product.objects.get(id = productid)
    print(productid , user)
    Cart(user = user , product = product).save()
    return redirect('/showcart')

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user = user)
        amount = 0.0
        shipping_amount = 0.0
        totalamount = 0.0
        cart_product = [p for p in Cart.objects.all() if  p.user == user ] #getting all the 
        
        if cart_product:
            for p in cart_product:
                tempamt = (p.quantity* p.product.discounted_price)
                amount+=tempamt
                tempshippingamount = tempamt*0.04
                shipping_amount +=tempshippingamount
                totalamount = amount + shipping_amount
        
            return render(request, 'app/addtocart.html' , {'carts' : cart , 'totalamount' : totalamount , 'amount':amount , 'shippingamount': shipping_amount})
        else:
            return render(request , 'app/emptycart.html')
        

def plus_cart(request):
    user = request.user
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get( Q(product = prod_id)  &  Q(user = request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 0.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
            tempamt = (p.quantity* p.product.discounted_price)
            amount+=tempamt
            tempshippingamount = tempamt*0.04
            shipping_amount +=tempshippingamount
            total_amount = amount + shipping_amount
            
        data = {
            'quantity' : c.quantity,
            'amount': amount , 
            'totalamount': total_amount,
            'shippingamount': shipping_amount
            
        } 
        return JsonResponse(data)
    


    
    
def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
    add = Customer.objects.filter(user = request.user)
    return render(request, 'app/address.html' , {'add' : add ,'active':'btn-primary'})

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
        return render(request , 'app/profile.html' , {'form':form  , 'active':'btn-primary'  })
    
    def post(self , request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user = usr , name = name , locality = locality  , city = city , state = state , zipcode  = zipcode)
            reg.save()
            messages.success(request , 'Profile Updated Successfully')
            
        return render(request , 'app/profile.html' , {'form' : form , 'active':'btn-primary'})
            
        
    
    
    
    




def checkout(request):
 return render(request, 'app/checkout.html')



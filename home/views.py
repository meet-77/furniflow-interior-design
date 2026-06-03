from django.shortcuts import render , redirect
from home.models import *
from django.contrib.auth.models import User 
from django.contrib import messages  
from django.contrib.auth import authenticate ,login , logout
from django.contrib.auth.decorators import login_required
 


# @login_required(login_url="/login/")
def hero(request):
    # herosection = Herosection.objects.all()
    latest_hero = Herosection.objects.order_by('-id').first() 
    detail = Product_detail.objects.order_by('-id')[:1]
    product = Product.objects.order_by('-id')[:3] 
    service = Service.objects.order_by('-id')[:4] 
    service_image = Service_image.objects.order_by('-id')[:1]
    design = Design.objects.order_by('-id')[:1]
    design_image = Design_image.objects.order_by('-id')[:3]
    design_text = Design_subtext.objects.order_by('-id')[:4]
    about = About.objects.order_by('-id')[:3]
    testimonual = Testimonial.objects.all()
    blog = Blog.objects.order_by('-id')[:3]
    context = {
                'hero': latest_hero,
                'detail':detail,
                'product':product,
                'service':service,
                'service_image':service_image,
                'design':design,
                'design_image':design_image,
                'design_text':design_text,
                'about':about,
                'testimonual':testimonual,
                'blog':blog,
            }
    return render(request, 'index.html', context)


def Login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/home/')  # Or use: return redirect('home') if named
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
               
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=second_name
        )
        
        return redirect('/login/')
    return render(request , 'register.html')


def logout_page(request):
    logout(request)
    return redirect("/login/")


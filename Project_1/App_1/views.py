import email
from telnetlib import LOGOUT
from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import auth
from App_1.models import Contact
from django.contrib import messages #For displaying message alert
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Book
from django.contrib.auth import get_user_model
from django.conf.urls.static import static 
User = get_user_model()

# Create your views here.
def index(request):
    books=Book.objects.all()
    print(books)
    params={'book':books}
    return render(request,'index.html',params)
def about(request):
    return render(request,'about.html')
def add_book(request):
    if request.method=="POST":
        book_isbn=request.POST.get('book_isbn')
        book_name=request.POST.get('book_name')
        pub_date=request.POST.get('pub_date')
        book_price=request.POST.get('book_price')
        book_des=request.POST.get('book_des')
        image=request.FILES['image']
        add_book=Book(book_isbn=book_isbn,book_name=book_name,pub_date=pub_date,book_price=book_price,book_des=book_des,image=image) #creating object of contact
        add_book.save() #saving all the info
        messages.success(request, 'Your form has been sent successfully!')
    return render(request,'add_book.html')
def admin_main(request):
    return render(request,'admin_main.html')
def services(request):
    return render(request,'services.html')
def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contactus=Contact(name=name,email=email,phone=phone,desc=desc) #creating object of contact
        contactus.save() #saving all the info
        messages.success(request, 'Your form has been sent successfully!')
    return render(request,'contactus.html')
def engineering(request):
    return render(request,'eng.html')
def admin_login(request):
    user=None
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None and user.is_active:
            if user.is_superuser or user.is_librarian:
                return redirect("/admin_main")
            else:
                messages.warning(request, 'Sorry! You have entered invalid credentials')
        else:
            messages.warning(request, 'Sorry! You have entered invalid credentials')
            return redirect("/admin_login")
    return render(request,'admin_login.html')
def loginuser(request):
    user=None
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None and user.is_active:
            if user.is_superuser:
                messages.warning(request, 'Sorry! You have entered invalid credentials')
                return redirect("/loginuser")
            else:
                auth.login(request,user)
                messages.success(request,"Successfully Logged in!")
                return redirect("/home")       
        else:
            messages.warning(request, 'Sorry! You have entered invalid credentials')
            return redirect("/loginuser")
    return render(request,'loginuser.html')
def logoutuser(request):
    logout(request)
    messages.success(request,'Successfully Logged Out!')
    return render(request,'logoutuser.html')
def createacc(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        user_name=request.POST.get('user_name')
        your_email=request.POST.get('your_email')
        your_pass=request.POST.get('your_pass')
        cnf_pass=request.POST.get('cnf_pass')
        user = User.objects.create_user(user_name, your_email,your_pass)
        user.first_name=fname
        user.last_name=lname
        user.save()
        messages.success(request,"Your Profile has been successfully created!")
        return redirect('/loginuser')
    return render(request,'createacc.html')
def engineering(request):
    return render(request,'eng.html')
def science(request):
    books=Book.objects.all()
    print(books)
    params={'book':books}
    return render(request,'sci.html',params)
def agriculture(request):
    books=Book.objects.all()
    print(books)
    params={'book':books}
    return render(request,'agr.html',params)
def architectural(request):
    return render(request,'arc.html')
def management(request):
    return render(request,'mng.html')

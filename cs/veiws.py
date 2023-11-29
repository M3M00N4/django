from django.shortcuts import render
def index(request):
    return render(request,"Demo.html")
def about(request):
    return render(request,"aboutus.html")
def userinput(request):
    return render(request,"userinput.html")
def veiwdata(request):
    email= request.GET['email']
    password=request.GET['password']
    data={
        'email' :email,
        'password' :password

    }
    return render(request,"veiwdata.html",data)

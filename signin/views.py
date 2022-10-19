from django.shortcuts import  render,redirect
from signin.forms import siginupForm
from django.contrib import messages
from django.contrib.auth import logout,authenticate, login


        
def newreg(request):
    form=siginupForm()
    if request.method=='POST':
        form=siginupForm(request.POST)
        user=form.save()
        user.set_password(user.password)

        user.save()
        return redirect('/login')
    else:    
        return render(request,"base.html",{'form':form})

        
def userlogin(request):
    if request.method=="POST":
        uname=request.POST.get("Uname")
        pa=request.POST.get("Pw")
        print(uname,pa)
        user = authenticate(username=uname, password=pa )
        #user = newregstration(email=uname, password=pa )
        if user is not None:
        # A backend authenticated the credentials
            login(request,user)
            print('i am logged')
            return redirect("/sh/show/")
        else:
            return render(request,"login.html")  
    else:
        return render(request,"login.html")


def userlogout(request):
    logout(request)
    return redirect("/login")


def home(request):
    messages.success(request,'UPLOAD your details.')
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        return render(request,'login.html')




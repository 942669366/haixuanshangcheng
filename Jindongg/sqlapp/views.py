from django.shortcuts import render
from sqlapp.models import User
from django.http import response

# Create your views here.
def BOSS(request):
    return render(request,"BOSS.html")



def login(request):
    username=request.POST.get("username")#获取文本框里面的用户名
    password=request.POST.get("password")#获取文本框里面的密码
    checkcode=request.POST.get("checkcode")#获取文本框里面的验证码
    usernames=User.useru.names()
    passwords=User.useru.passw()

    return render(request,"login.html")

def regist(request):
    if request.method == "POST":
        username = request.POST.get("username")  # 获取文本框里面的用户名
        password=request.POST.get("password")#获取文本框里面的密码
        print(username,password)
        # password2 = request.POST.get("password2")  # 获取文本框里面的密码
        # checkcode=request.POST.get("checkcode")#获取文本框里面的验证码
        mess=User.useru.insert(username,password)
        print(mess)
        if mess == "注册成功":
            a= "BOSS"
        else:
            a= "regist"
        return render(request,"BOSS.html",{"mess":mess, "a":a})
    else:
        return render(request, "regist.html", )


def flow1(request):
    return render(request,"flow1.html")
def flow2(request):
    return render(request,"flow2.html")
def flow3(request):
    return render(request,"flow3.html")
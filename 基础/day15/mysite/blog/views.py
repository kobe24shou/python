from django.shortcuts import render,HttpResponse
from blog import models
import datetime


# Create your vies here.

def cur_time(request):  # 创建函数去处理 对应的url
    times = datetime.datetime.now()  # 拿到变量，然后嵌套到html文件的变量里面去
    # return HttpResponse("<h1>ok</h1>")

    return render(request,"cur_time.html",{"abc":times},) # 映射关系 abc 是给前端的

user_list=[]

def userInfo(req):

    if req.method == "POST":
        username = req.POST.get("username",None)
        sex = req.POST.get("sex",None)
        mail = req.POST.get("mail",None)

        #user = {"username":username,"sex":sex,"mail":mail}
        #user_list.append(user)

        # create 是插入数据

        models.UserInfo.objects.create(
        username=username,
        sex=sex,
        email=mail
        )

    user_list = models.UserInfo.objects.all()

    return render(req,"index.html",{"user_list":user_list})

def special_case_2003(req):
    return  HttpResponse("2003")

def year_archive(req):
    return  HttpResponse("Year")

def year_archive1(req,year):
    return  HttpResponse(year+"Year")
# year 接收的是前端传过来的字符串

def month_archive(req,y,m):
    return HttpResponse(y+"||"+m+"month")
#  urls里面 2个括号就有要传2个参数  y 和 m 有位置关系

def article_detail(req,year,month,day):
    return HttpResponse(year+"||"+month+"month"+day+"day")
# 名字不能随便取，必须安装urls 的名字来

def index1(req,name):
    return  HttpResponse(name)

def index(req):
    print("req.GET ====>",req.GET)
    print("req.POST ====>",req.POST)
    print("req.path ====>",req.path)

    if req.method=='POST':
        username=req.POST.get('username')
        password=req.POST.get('password')
        if username=='ls' and password=='123':
            return HttpResponse("登陆成功")
        else:
            print(username,password)

    return render(req,'login.html')

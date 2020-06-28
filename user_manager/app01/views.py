from django.shortcuts import render,redirect,HttpResponse
from app01 import  models
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def test(request):
    # return HttpResponse ('OK')
    obj =  HttpResponse ('OK')
    obj.set_cookie('k1','v1')
    return  obj

def xiaohu(request):
    v = request.COOKIES.get('k1')
    return  HttpResponse(v)

def login(request):
    # 创建用户
    # models.Administrator.objects.create(
    #     username = 'xxx',
    #     password = '123123'
    # )
    message = ""
    print(request.method)
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        c = models.Administrator.objects.filter(username=user,password=pwd).count()
        #if user == 'root' and  pwd == 'root':
        if c:
            # 在神奇的地方放置当前的用户名
            # 神奇的地方在用户的浏览器上
            # max_age=10 设置cookie 只保留10秒
            rep = redirect('/index.html')
            rep.set_cookie('username',user,max_age=10)
            rep.set_cookie('email',user+"@live.com")

            return  rep
        else:
            message = "用户名或密码错误"
    return  render(request,'login.html',{'msg':message})


def index(request):
    #如果用户已经登陆，获取当前登陆的用户名
    #否则，返回登陆页面
    print(request.COOKIES)

    username = request.COOKIES.get('username')
    if username:
        return render(request,'index.html',{'username':username})
    #username = "ls"
    else:
        return redirect('/login.html')

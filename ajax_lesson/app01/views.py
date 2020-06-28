from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(req):

    return render(req,"index.html")

def ajax_receive(req):

    return HttpResponse("HELLO xx")


def login(request):
    print('hello ajax')
    return render(request,'index.html')
    # return HttpResponse('helloyuanhao')

@csrf_exempt
def ajax_register(request):
    print('ok')

    if request.method =="POST":
        username=request.POST.get('username',None) # 拿到后端传过来的 username
        if username=='xx':
            return HttpResponse('true') # 返回前端只告诉存在还是不存在
        return HttpResponse('false')

    return  render(request,"register.html")
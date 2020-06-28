from django.shortcuts import render

# Create your views here.

def xiaohu(req):
    print('前端数据POST',req.POST)
    print('前端数据GET',req.GET)

    print("file:",req.FILES)  # 文件内容对象

    for item in req.FILES:
        obj = req.FILES.get(item,None)
        filename = obj.name

        f = open(filename,'wb')
        for line in obj.chunks():
            f.write(line)

        f.close()

    return  render(req,"index.html")
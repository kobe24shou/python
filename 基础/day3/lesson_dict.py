#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:ls 
# aishou24@gmail.com
# date:2018/3/9

#__author:  Administrator
#date:  2016/8/23

#字典两大特点：无序，键唯一

#创建字典
dic={1:'alex','age':35,'hobby':{'girl_name':'铁锤','age':35},'is_handsome':True}
dic1={'age11':'alex','age12':35,'hobby':{'girl_name':'铁锤','age':45},'is_handsome':True}

print(dic)
print(dic1)
print(id(dic))  #打印内存地址
print(dic['hobby']) #key 一定要是不可修改的数据类型

a=list((1,2,3,5)) #创建列表
print(a)

#字典的创建
#两种创建方法
dic11={'name':'alex'}
dic21=dict((('name','alex'),('xx','tt'))) #工厂函数
print(dic11)
print(dic21)

dic31=dict([['name','alex']])
print(dic31)


print('==============================================')
#字典元素添加,如果存在，就是修改了
dic12={'name':'alex'}
dic12['age']=18
print(dic12)
print('======================增加========================')

#键存在，不改动，返回字典中相应的键对应的值
ret=dic12.setdefault('age',34)
print(ret)  #setdefault有返回值 ，返回键的值
#
##键不存在，在字典中中增加新的键值对，并返回相应的值
ret2=dic12.setdefault('hobby','girl')
print(dic12)
print(ret2)

print('======================查========================')
#查  通过键去查找
dic33={'age': 18, 'name': 'alex', 'hobby': 'girl'}
print(dic33['name'])
print(dic33.keys()) #查看字典所有的建值
print(list(dic33.keys())) #查看字典所有的建值
print(list(dic33.values())) #查看所有的值
print(list(dic33.items())) #查看字典所有的项

print('======================改========================')

#跟列表类似
li=[1,2,34,4]
li[2]=5
print(li)

dic34={'age': 18, 'name': 'alex', 'hobby': 'girl'}
dic34['age']=55
print(dic34)

dic44={'age': 18, 'name': 'alex', 'hobby': 'girl'}
dic54={'1':'111','2':'222'}
dic54={'1':'111','name':'222'}
dic44.update(dic54) # 把dic54 加入 到 dic44 里面，如果有相同key， 也会更新掉
print(dic44)
print(dic54)

print('======================删除========================')

dic55 = {'name': 'alex', 'age': 18, 'class': 1}

dic55.clear() # 清空字典
print(dic55)
dic55 = {'name': 'alex', 'age': 18, 'class': 1}
del dic55['name'] #删除字典中指定键值对
print(dic55)

dic55 = {'name': 'alex', 'age': 18, 'class': 1}
print(dic55.pop('age')) #删除字典中指定键值对，并返回该键值对的值
#ret55=dic55.pop('age')
#print(ret55)
print(dic55)

dic55 = {'name': 'alex', 'age': 18, 'class': 1}
a = dic55.popitem() #随机删除某组键值对，并以元组方式返回值
print(a, dic55)

del dic55        #删除整个字典


#5 其他操作以及涉及到的方法
print('======================其他操作========================')


dic6=dict.fromkeys(['host1','host2','host3'],'test') #前面统一为建，后面为统一的值，初始化
print(dic6)#{'host3': 'test', 'host1': 'test', 'host2': 'test'}
#
dic6['host2']='abc'
print(dic6)

dic66=dict.fromkeys(['host1','host2','host3'],['test1','tets2'])
print(dic66)#{'host2': ['test1', 'tets2'], 'host3': ['test1', 'tets2'], 'host1': ['test1', 'tets2']}
#
dic67=dict.fromkeys(['host1','host2','host3'],['test1','tets2'])
dic67['host2'][1]='test3'
print(dic67)#{'host3': ['test1', 'test3'], 'host2': ['test1', 'test3'], 'host1': ['test1', 'test3']}



#大的数据字典  里面又嵌套的列表
av_catalog = {
     "欧美":{
         "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
         "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
         "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
         "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
     },
     "日韩":{
         "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
     },
     "大陆":{
         "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
     }
}

#修改
av_catalog['欧美']["www.youporn.com"][1]='高清WWWWWWWWWWWWWWW午马'
print(av_catalog)


print('==============================================================')

dic88={5:'555',2:'666',4:'444'}
print(sorted(dic88.items()))  #排序


print('=============================for 输出=================================')

dic59={'name': 'alex', 'age': 18}
for i in dic59:
     print(i,dic59[i]) #这种效率比下面的高一些

for i,v in dic59.items():
     print(i,v)


print('=============================String 操作=================================')
a="Let's go "
print(a)
# 1  * 重复输出字符串
print('hello'*20)

# 2 [] ,[:] 通过索引获取字符串中字符,这里和列表的切片操作是相同的,具体内容见列表
print('helloworld'[2:])

#关键字 in
print(123 in [23,45,123])
print('e2l' in 'hello')

# 4 %   格式字符串
print('alex is a good teacher')
print('%s is a good teacher'%'alex')

#5 字符串连接
a='123'
b='abc'
d='44'
# c=a+b
# print(c)
c= ''.join([a,b,d]) # 这种写法效率比上面的高一些
print(c)

print('=============================String的内置方法=================================')

# String的内置方法
st='hello kitty {name} is {age}'

print(st.count('l'))       #  统计元素个数
print(st.capitalize())     #  首字母大写
print(st.center(50,'#'))   #  居中
print(st.endswith('tty3')) #  判断是否以某个内容结尾
print(st.startswith('he')) #  判断是否以某个内容开头，常用于文件处理的判断标志
print(st.expandtabs(tabsize=20))
print(st.find('t'))        # 8  查找到第一个元素，并将索引值返回
print(st.format(name='alex',age=37))  # 格式化输出的另一种方式   待定：?:{}
print(st.format_map({'name':'alex','age':22})) # map 后面放一个字典 上面是赋值，下面是字典，形式不一样而已
print(st.index('t')) #INDEX找不到就报错，find 不会报错
print('=============================String的内置方法222=================================')
print('asd'.isalnum())
print('12632178'.isdecimal())
print('1269999.uuuu'.isnumeric())
print('1999'.isdigit())
print('abc'.isidentifier())
print('Abc'.islower())
print('ABC'.isupper())
print('  e'.isspace()) #是否是个空格
print('My title'.istitle())
print('My tLtle'.lower())
print('My tLtle'.upper())
print('My tLtle'.swapcase())
print('My tLtle'.ljust(50,'*'))
print('My tLtle'.rjust(50,'*'))
print('\tMy tLtleyyy\n'.strip())
print('\tMy tLtle\n'.lstrip())
print('\tMy tLtle\n'.rstrip())
print('ok')
print('My title title'.replace('itle','lesson',1))
print('My title title'.rfind('t'))
print('My title title'.split('i',1))
print('My title title'.title())

print('=============================重要的字符串方法=================================')
#摘一些重要的字符串方法
print(st.count('l'))
print(st.center(50,'#'))   #  居中
print(st.startswith('he')) #  判断是否以某个内容开头
print(st.find('t'))
print(st.format(name='alex',age=37))  # 格式化输出的另一种方式   待定：?:{}
print('My tLtle'.lower())
print('My tLtle'.upper())
print('\tMy tLtle\n'.strip())
print('My title title'.replace('itle','lesson',1))
print('My title title'.split('i',1))
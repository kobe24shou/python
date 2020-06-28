from django.test import TestCase

# Create your tests here.
import re

ret=re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt123/ooo')
# ?P 固定格式 <id>是对应的组  \d{3} 匹配3个数字  \w{3} 匹配3个非数字的字符
print(ret.group()) #123/ooo
print(ret.group('id')) # 123
print(ret.group('name')) # ooo
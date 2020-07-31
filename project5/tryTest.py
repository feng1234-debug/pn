#coding=utf-8

#aythor:fengzixian
#异常的概述和讲解
def div(a,b):
    return a/b

'''
1.try代码执行正常，就不会执行expect的代码
2.只有try代码执行异常，就会执行except的代码
'''
# try:
#     div(1,0)
# except KeyError as e:
#     print()
# except ValueError as e:
#     print()
# except WindowsError as e:
#     print()
# except ZeroDivisionError as e:
#     print(e.args)



# def f(*args,**kwargs):
#     return kwargs
# return f('231321')

'''
业务：
1.功能
2.接口
1.JS代码不能出问题
2.前后交互不能出问题
3.场景化，流程，逻辑不能出问题
4.高频的用户场景
'''

try:
    div(1,0)
except Exception as e:
    print(e.args)
    raise ('对八起，我不在')
else:
    print('pass')
finally:
    print('finally')
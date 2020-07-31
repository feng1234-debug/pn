#coding=utf-8
'''
根据字符串的形势去某个模块中寻找XX函数----getattr()
根据字符串的形势去某个模块中判断东西是否存在---hasattr()
根据字符串的形势去某个模块中设置东西---setattr
根据字符串的形式去某个模块中删除东西---delattr
'''
# #通过__import__导入目标模块并且放在一个对象中
# f=__import__('login')
# #通过对象找login模块中index的字符并且调用
# f.index()
# import login
# f=getattr(login,'logout')
# f()

#import login

# obj=login.Person()
# #hasattr从元素中判断元素是否存在，getattr该元素
# if hasattr(obj,'info'):
#     f=getattr(obj,'info')
#     f()
# else:
#     print('sorry')

# obj=login.Person()
# f=setattr(obj,'exit','this is a exit method')


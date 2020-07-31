#coding=utf-8

# def read():
#     with open('c:/log.txt','r') as f:
#         return f.read()
#
# def write():
#     with open('c:/log.txt','w') as f:
#         return f.write()
#
# def write2():
#     with open('c:/log.txt','a') as f:
#         return f.write()


# class FileOperation(object):
#     def __init__(self,filename):
#         '''
#         :param filename: 要操作的文件
#         '''
#         self.filename=filename
#
#     def read(self):
#         with open(self.filename,'r') as f:
#             return f.read()
#
#     def write(self,content):
#         with open(self.filename,'w') as f:
#             f.write(content)

'''
类：客观存在的抽象事物
对象：对类实例化后的变量

封装的思想，
1.同样的操作行为放在一个类中
2.把公共的参数封装到类的初始化方法中
'''

# f=FileOperation('C:/log.txt')
# # f.write('fengmei')
# # f.filename='C:/log.txt'
# print(f.read())

# class Person(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def show(self,school):
#         print('姓名:{0},年龄:{1},学校:{2}').format((self.name,self.age,school))
#
#     def post(self,**kwargs):
#         print(kwargs)
#
# obj=Person('feng',19)
# obj.post(**{'name':'feng','age':18})

# import requests
# requests.post()

'''
类：
1.子类优先考虑调用自己的方法-----→从下到上的原则
2.当一个类被多个类继承的时候，会根据类的列表顺序调用方法----从左到右的原则
'''
# class Person(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def info(self):
#         print('姓名:{0},年龄:{1}').format((self.name,self.age))
#
# class Usa(Person):
#     def __init__(self,name,age,sex):
#         self.sex=sex
#         Person.__init__(self,name,age)
#
#     def info(self):
#         print('姓名:{0},年龄:{1},性别:{2}'.format(self.name,self.age,self.sex))
#
# per=Usa('feng',18,'gril')
# per.info()


'''
多继承
python2 深度优先
python3 广度优先
'''

class A(object):
    def test(self):
        print('A')

class B(A):
    pass

class C(A):
    def test(self):
        print('C')

class D(B,C):
    pass
d=D()
d.test()


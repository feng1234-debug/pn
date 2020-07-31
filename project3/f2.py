#coding=utf-8

'''
需求：要求注册账户，然后注册的账户登录到系统后，显示出登录的昵称
1.注册的函数
2.登录的函数
3.获取昵称的函数
'''

def Inout():
    username = input('username:\n')
    password = input('password please:\n')
    return username,password

def register():
    username, password = Inout()
    temp=username+'|'+password
    with open('login.md','w') as f:
        f.write(temp)

def login():
    '''登录函数'''
    username,password=Inout()
    with open('login.md','r') as f:
        info=f.read()
        info=info.split('|')
    if username==info[0] and password==info[1]:
        return True
    else:
        return False

def getNick(func):
    '''获取昵称'''
    with open('login.md','r') as f:
        info=f.read()
    info=info.split('|')
    if func:
        print('{0}您好，欢迎您登录'.format(info[0]))
    else:
        print('请登录')

# if __name__=='__main__':
def main():
    while True:
        try:
            t=input('1.注册 2.登录 3.退出系统\n')
            #如果是float类型的处理
            if isinstance(t,float):
                t=int(t)
            elif isinstance(t,str):
                #判断字符串是否大于1位，如果是，取出第一位，并把字母转为数字
                if len(t)==1:
                    t=ord(t)
                else:
                    t=int(ord(list(t)[0]))
        except Exception as e:
            print(e.args)
        else:
            if t==1:
                register()
            elif t==2:
                getNick(login())
            elif t==3:
                import sys
                sys.exit()
            else:
                print('请注册！')
        finally:
            pass
main()

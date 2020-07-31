#coding=utf-8

import pymysql

# #查询
# def connMySQL():
#     try:
#         conn=pymysql.connect('localhost','root','admin')
#         conn.select_db('five')
#     except Exception as e:
#         return e.args
#     else:
#         cur=conn.cursor()
#         cur.execute("select * from users")
#         data=cur.fetchall()
#         # for item in data:
#         #     print(item)
#         #列表推导式
#         db=[item for item in data]
#         print(db)
#         # 打开之后进行关闭，不然会占用资源
#     finally:
#         cur.close()
#         conn.commit()
#         conn.close()
#
# print(connMySQL())



# #插入数据
# def insertMySql():
#     try:
#         conn=pymysql.connect('localhost','root','admin')
#         conn.select_db('five')
#     except Exception as e:
#         return e.args
#     else:
#         cur=conn.cursor()
#         #单条插入
#         # sql='insert into users values (%s,%s,%s,%s)'
#         # params=(12,'wei',99,'changjiang')
#         #多条插入
#         sql = 'insert into users values (%s,%s,%s,%s)'
#         params=[(13,'wei',99,'changjiang'),(14,'wei',99,'changjiang'),(15,'wei',99,'changjiang')]
#         cur.executemany(sql,params)
#         conn.commit()
#         # 打开之后进行关闭，不然会占用资源
#     finally:
#         cur.close()
#         conn.close()
#
# insertMySql()

#插入数据

# #删除数据
# def deleteMySql():
#     try:
#         conn=pymysql.connect('localhost','root','admin')
#         conn.select_db('five')
#     except Exception as e:
#         return e.args
#     else:
#         cur=conn.cursor()
#         #多条插入
#         cur.execute = 'delete * from users where id= 1'
#         conn.commit()
#         # 打开之后进行关闭，不然会占用资源
#     finally:
#         cur.close()
#         conn.close()
#
# deleteMySql()


class MySqlHelper:
    def conn(self):
        con=pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='admin',
            db='aimin')
        return con

    def get_one(self,sql,params):
        cur=self.conn().cursor()
        data=cur.execute(sql,params)
        result=cur.fetchone()
        return result

def checkValid(username,password):
    opera=MySqlHelper()
    sql='select * from login where username=%s and password=%s'
    params=(username,password)
    return opera.get_one(sql=sql,params=params)

def info():
    username=input('请输入用户名：\n')
    password=input('请输入密码：\n')
    result=checkValid(username,password)
    if result:
        print('登录成功，昵称：{0}'.format(username))
    else:
        print('失败')

if __name__=='__main__':
    info()

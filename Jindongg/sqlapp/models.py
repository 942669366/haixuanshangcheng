from django.db import models

# Create your models here.

class StudentManager(models.Manager):#定义一个函数，继承model函数，目的就是在使用model函数的基础上面新增一些自己添加的功能
    def names(self):#返回数据库里的stuname值的函数
        stunamelist=[]
        for stu in  self.all():
          stunamelist.append(stu.username)
        return stunamelist

    def passw(self):#返回数据库里面的stuid 的值的函数
        idlist=[]
        for stu in  self.all():
           idlist.append(stu.password)
        return idlist

    def insert(self,username,password):
        idlist=self.names()

        if username in idlist:
            print("2222222")
            return "请重新注册"
        else:
            print("33333")
            User(username=username,password=password).save()
            return "注册成功"

class User(models.Model):
    useru=StudentManager()
    username=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=12)

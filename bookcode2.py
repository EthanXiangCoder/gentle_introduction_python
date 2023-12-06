from string import Template
import math
from math import e
from random import choice
from abc import ABC,abstractmethod
from warnings import warn,filterwarnings 
import collections

# 三种设置字符串的方式

# value = ("xiang", "wei")
# sent = "hello %s, my name is %s"
# print(sent%value)

# sent = Template("hello $name1,my name is $name2")
# print(sent.substitute(name1="xiang", name2="wei"))

# print(f"the original e is {e:.2f}")
# print("hello {1},my name is {0}".format("xiang","wei"))

# print("the {mod.__name__} module defines the e is {mod.e}".format(mod = math))

#字符串部分串接使用字符串的一个作业 输出一个价格表
# total_width = 35
# forward_width = 10
# back_width = total_width-forward_width

# namecolumn = "{{:{}}}{{:>{}}}".format(forward_width,back_width)
# contentcolumn = "{{:{}}}{{:>{}.2f}}".format(forward_width,back_width)

# print("="*total_width)

# print(namecolumn.format("Fruit","Price"))

# print("="*total_width)

# print(contentcolumn.format("Apple",3.1564522))
# print("-"*total_width)

# print(contentcolumn.format("Orange",2.64564))
# print("-"*total_width)

# print(contentcolumn.format("Pinapple",8.0))
# print("="*total_width)

#这里写一下简单推理的一个例子
#比较简单的代码例子如下：
# boys = ["aley", "bob", "clark"]
# girls = ["alice", "brown", "cray"]
# print([b+"+"+g for b in boys for g in girls if b[0]==g[0]])

#比较有效率的寻找方法就是设置一个信使】
# boys = ["aley", "bob", "clark"]
# girls = ["alice", "brown", "cray"]
# girlletters = {}
# for g in girls:
#     girlletters.setdefault(g[0],[]).append(g)
# print([b+"+"+gi for b in boys for gi in girlletters[b[0]] ])

#判断一个变量是不是可调用的
# x = 1
# y = math.sqrt #注意这里不能写math.sqrt() 这样就是调用函数了
# print(callable(x),callable(y))

# def calculate(x):
#     "calculate the sqrt of x"   #文档字符串 对函数做出申明
#     return x**2

# print(calculate.__doc__)  #可调用__doc__看到文档字符串的内容

#这里需要再次强调，字符串和元组是一样的，原则上不调用方法是不可更改的
#这里用几段代码说明一下函数调用时实参和形参是怎么相互影响的

# string = "alice"
# def change(x):
#     x = "aaaa"
#     return
# change(string)
# print(string) #还是会输出alice 因为这个函数调用和下面的代码是一样的:

# string = "alice"
# x = string
# x = "aaaa"
# print(string)

#但如果是一个可循环的对象且只更改部分时会出现不同
# strings = ["aaaa","bbbb","cccc"]
# def change(x):
#     x[0] = "dddd"
# change(strings)
# print(strings) #会输出"dddd" 原因不多说了前面说过： 等同于下面这个

# string = ["aaaa","bbbb","cccc"]
# x = string
# x[0] = "dddd"
# print(string)

#如果我想实现一个给定名字中的部分信息，就能从数据库中查找所有的相关人名的算法 我一定是通过字典实现
# storge = {}
# storge["first"] = {}
# storge["second"] = {}
# storge["third"] = {}

# name1 = "Michael B Jordan"
# nameparts = name1.split()
# storge["first"].setdefault(nameparts[0],[]).append(name1)
# storge["second"].setdefault(nameparts[1],[]).append(name1)
# storge["third"].setdefault(nameparts[2],[]).append(name1)

# print(storge["second"]["B"])  #这样的编写效率难免低下 因此提出使用三个函数进行改进 隐藏实现细节

# storge = {}

# def init(data):
#     data["first"] = {}
#     data["second"] = {}
#     data["third"] = {}

# init(storge)

# def search(data,label,namepart):
#     return data[label].get(namepart)

# def save(data,name):
#     namelists = name.split()
#     if len(namelists)==2:
#         namelists.insert(1," ")
#     parts = ["first","second","third"]
#     for part,namelist in zip(parts,namelists):
#         now = search(data,part,namelist)
#         if now:
#             data[part][namelist].append(name)
#         else:
#             data[part][namelist] = [name]

# save(storge,"Michael B Jordan")
# save(storge,"Michael Jordan")

# print(search(storge,"first","Michael"))


#下面也是一个很重要的部分，就是关键字参数和默认值
#下面两个代码比较接近是非常出错的：
# def print1(str1,str2):
#     print("hello {},this is {}".format(str1,str2))
# def print2(str1,str2):
#     print("hello {},this is {}".format(str2,str1)) #如果程序比较大 这两个相近的代码十分容易出错，因此我们使用关键词参数来调用，这时就不需要管参数顺序了:

# print1(str1 = "xiang",str2 = "ethan")
# print2(str2 = "xiang",str1 = "ethan")

# #同时关键字参数还有一个非常好的用法 就是指定默认值 并且可以任意修改默认值的个数

# def print3(str1 = "ethan", str2 = "xiang"):
#     print("hello {}, this is {}".format(str1, str2))

# print3("alice") #值得说明的是 如果你只喂入一个参数 那么会默认读入第一个形参中 如果想输入的实参是喂入的第二个或者其他位置的形参 就可以用关键字参数说明 
# #同时如果有多个参数 有一部分是给了默认值的话 那么函数调用的时候会优先给到没给默认值的形参
# print3()
# print3("clai","dsjdasd")

#收集和分配参数
#首先说明一个收集参数的写法 可以尝试一下下面的这段代码：
# def print1(*x):
#     print(x)

# print1("dshkdj")  #这里会输出("dshkdj",)即一个元组 其实就是 在函数定义的时候，前面加一个*号 会同时读入多个值，并将其存在一个tuple中 

# def print2(y,z, **x):
#     print(y)
#     print(x)

# print2("dsdjs","jjjf") #这里就会出错 因为前面加*的部分是不可以喂入关键字参数的，这里类似于一个key 和 value 对应的关系 #同时这里是不能将其命名为y的(当使用**的时候 会二次读入)

#当我们想要输入一个关键字参数的时候 就需要用到和刚才比较接近的思想：用一个字典去存储 使用**去收集参数
#下面说一个特殊的例子：
# def print3(x,*y,z):
#     print(x)
#     print(y)
#     print(z)

#print3("dsjds","dsjd","ddd")#像这样写是会直接报错的 当收集参数在中间时，因为代码不知道在哪里停下来 所以必须用关键字参数指定最后的参数
#print3("dsjf",z= "ddd")

#接下来说分配参数 这里就有点类似前面说过的序列解包
# def print4(x, y):
#     print(x)
#     print(y)

# print4(*("fdfd","ggg")) #起到一个分配参数的作用
# #那么同理 如果要将一个字典分配到函数中使用 则可以通过**来完成
# dict1 = {"x":"ddd","y":"sss"}
# print4(**dict1) #一定要注意这里的分配 如果我将value名命名为函数中不知道的key值 他将识别不了并报错

#由此我们能改写之前的输入名字的代码
# storge = {}
# def init(data):
#     data["first"] = {}
#     data["mid"] = {}
#     data["last"] = {}

# def search(data,part,partname):
#     return data[part].get(partname)

# def save(data,*names):
#     parts = ["first","mid","last"]
#     for name in names:
#         nameparts = name.split()
#         if len(nameparts)==2: nameparts.insert(1," ")
#         for namepart,part in zip(nameparts,parts):
#             key = search(data,part,namepart)
#             if key:
#                 data[part][namepart].append(name)
#             else:
#                 data[part][namepart] = [name]

# init(storge)
# save(storge,"Michael B Jordan","Michael Jordan")
# print(search(storge,"first","Michael"))
#命名空间的一些操作
#主要就是全局变量的一些操作
#在python中 声明的变量都是存在于一定的变量空间的 比如：
# x = 1
# y = vars()
# print(y["x"]) #要注意这里的调用方式

#现在比方说在代码里有这么一段：
# global_var = "sent"
# def print_v(part):
#     global_var = "send"
#     print(part,global_var)

# def print_v1(part):
#     global_var = "send"
#     print(part,globals()["global_var"])

# print_v("part") #一定会使用更小的空间内的变量 但这时如果改写一次代码
# print_v1("part") #即可使用全局变量

# #将函数当成变量的一些函数式编程
# print([str(x) for x in range(10)])
# print(list(map(str,range(10)))) #两者类似 功能就是将函数变量施加到后面的序列或视图中

# def isOu(x):
#     return x%8==0 

# print(list(filter(isOu,[x*x for x in range(10)])))

# class MemberNum:
#     num = 0
#     def numchange(self):
#         self.num += 1

# m1 = MemberNum()
# m1.numchange()

# print(m1.num)
# print(MemberNum.num)

# m2 = MemberNum()
# m2.numchange()

# print(m2.num)
# print(MemberNum.num)

# class MemberNum1:
#     num = 0
#     def numchange(self):
#         MemberNum1.num += 1

# m1 = MemberNum1()
# m1.numchange()

# print(m1.num)
# print(MemberNum1.num)

# m2 = MemberNum1()
# m2.numchange()

# print(m2.num)
# print(MemberNum1.num)  #这几个例子是想说明类属性和实例属性之间的关系

# try:
#     3/0
# except ZeroDivisionError:
#     raise ValueError from None

#异常是可以写多个的
# try:
#     x = input("the number of x is: ")
#     y = input("the number of y is: ")
#     x/y
# except ZeroDivisionError:
#     print("Error!")
# except TypeError:
#     print("Error too!") #再次说明 这样的代码仅仅只是捕获异常 但并不是直接终止代码 所以还是需要raise来引发异常 如果不编写raise引发异常 函数会自动返回一个None值

# try:
#     x = input("the number of x is: ")
#     y = input("the number of y is: ")
#     x/y
# except (ZeroDivisionError,TypeError,ValueError):
#     print("Error!")   #也可以写成一个tuple 同时指定多个错误类型 或直接不写 这代表捕获exception下的所有派生错误

# while True:
#     try:
#         x = int(input("the number of x is: "))
#         y = int(input("the number of y is: "))
#         x/y
#     except Exception as e:
#         print(e)
#     else:
#         break                

#最后在这类语句中还有一个finally 这个是在结束之后都会执行的 通常处理一些后处理场景

# x = None
# try:
#     x = 1/0
# finally:
#     del x
#     print("something wrong")

#类部分经常用的属性和函数 
# class demo:
#     def init(self,innum="a"):
#         self.data = innum
#     def showdemo(self):
#         print(self.data)

# class demosample(demo):
#     def __init__(self):
#         super().__init__

# print(issubclass(demosample,demo)) #True
# print(issubclass(demo,demosample)) #False

# d = demosample()
# print(isinstance(d,demosample)) #True
# print(isinstance(d,demo)) #True 由子类创建的实例也是超类的实例
# #isinstance甚至可以用在内置类型中
# stringa = "string"
# print(isinstance(stringa,str))

# print(d.__dict__) #输出某个实例的全部属性
# d.__dict__["age"] = 10
# print(d.__dict__)  #可以直接像上面一样赋予实例的属性

# print(demosample.__bases__) #输出子类的超类 超类可以多重继承 可以有多个
# print(d.__class__) #输出实例的所属类

# '''先斩后奏 不显式编写接口 默认对象可以完成操作 "存取方法"
#    这里我觉得需要说明的是和后面有关特征编写的部分联系起来
#    一般的面向对象开发语言都会显示地编写类和函数接口以便代码当中使用 但python的逻辑是:我将类的实例赋值到函数的参数中进行使用 即使可能没有我想要的方法 但我默认他可以完成 如果不可以 则进行异常返回或者进行检查
# '''
# #借用前面的类实现
# print(hasattr(d,"age")) #True 有没有某项方法或属性
# print(hasattr(d,"showdemo")) #True

# print(getattr(d,"age",None)) #10 输出指定属性的值
# print(getattr(d,"height",None)) #None 输出没有属性的值 如果没有则输出第三个参数 
# '''这里有一些区别的地方在于:特征部分的__getattr__只获取未有的值 并且__getattr__可以改写一定的情况'''

# setattr(d,"age",20)
# print(getattr(d,"age",None)) #20 发生修改

# #抽象类
# #from abc import ABC,abstractmethod
# __metaclass__ = type
# class demoBase(ABC): #新式一般就写ABC即可 但python2.x的早期代码中一般创建新类时会在开头写上一句上面一行的代码 同时在超类这里写成 metaclass=ABCMeta
#     @abstractmethod  
#     def __init__(self):
#         super().__init__()
# #抽象类一般的作用就是去制定书写格式
# #下面再说一个对超类的理解
# class bird:
#     def fly(self):
#         self.canfly = True
#         print("i can fly")

# class smallbird(bird):
#     pass

# class chicken:
#     def fly(self):
#         self.alsocanfly = True

# #bird.register(chicken) 直接使用register是不太可取的 AttributeError
# '''这样处理使得chicken也成为bird的子类 但最大的问题就是 此时isinstance 和 issubclass并不能检测chicken的一些细节问题 会直接返回True 而两者的属性是不一样的'''

# #警告
# warn("this is a warning")
# filterwarnings("ignore") #两种警告模式 忽略就可以继续运行代码
# warn("we can ignore it")
# filterwarnings('error') #捕获异常就可以指定异常类型 并且报错
# warn("we need to solve it",TypeError)    

#重写构造函数的错误案例
# class demo:
#     def __init__(self): #__xxx__之类的都是特殊方法
#         self.caneat = True
#     def eat(self):
#         if self.caneat:
#             self.eating = False
#         else:
#             self.eating = False

# class demosample(demo):
#     def __init__(self,data):
#         self.dataset = data

# d = demosample("hahah")
# print(d.caneat) #AttributeError 因为重写了构造函数 所以之前的属性也会丢失 因此需要一定的手段 即使在修改构造函数的时候 也能继承之前的一些属性
        
#使用未关联的超类构造函数 名字唬人一行代码 老代码中常见
# class demo:
#     def __init__(self):
#         self.caneat = True
#     def eat(self):
#         if self.caneat:
#             pass
#         else:
#             print("ahhh")
#             self.caneat = True

# class demosample(demo):
#     def __init__(self):
#         demo.__init__(self)
#         self.canfly = True
#     pass

# d = demosample()
# print(d.caneat) #此时等于是继承了之前的init初始函数 即不会覆盖之前的Init函数

#super 重写构造函数
# class demo:
#     def __init__(self):
#         self.caneat = True
#     def eat(self):
#         if self.caneat:
#             pass
#         else:
#             print("aggg")
#             self.caneat = False

# class demosample(demo):
#     def __init__(self):
#         super(demosample,self).__init__()
#         self.canfly = True

# d = demosample()
# print(d.caneat)

#元素访问
#元素访问的第一部分 基本的序列协议（四种）代码：编写一个计数序列
'''这里说明一下 Python中并不是只有视图、序列、字符串等可以在一个循环中进行元素遍历 而是符合序列协议的类实例都是可以的 所以我们只需要学习怎么编写协议 即可自行组建可以顺序遍历的变量'''
#这四个方法不是都一定要实现 但当不实现时则不能进行相应的调用 注意都是特殊方法 所以直接可以简便使用 如果__len__没有编写则默认这个实例是无限长的
# class likelist:
#     def __init__(self,begin=0,step=2):
#         self.begin = begin
#         self.step = step
#         self.seq = {1:begin}
#         pass

#     def __len__(self):
#         return len(self.seq)
    
#     def __getitem__(self,num):
#         if self.seq.get(num,None):
#             return self.seq[num]
#         else:
#             self.seq[num] = self.begin+self.step*(num-1)
#             return self.seq[num]
    
#     def __setitem__(self,num,value):
#         self.seq[num] = value
#     '''最开始没有编写__delitem__函数'''

# l = likelist()
# print(l[5]) #8
# l[5] = 11
# print(l[5]) #11
# print(len(l)) #2
# '''del(l[2])''' #没编写__delitem__就会报错

#元素访问的第二部分，从collections模块或者内置类型继承获得超类方法定义 注意*args的用法，可以接收 这是对上面的扩展 特殊方法有很多 没办法全部进行改写 所以最好的方法是改写需要改写的 剩下的全部继承
# class CounterList(list):
#     '''定义一个特殊的会数数的列表
#         未被定义的部分会自动继承
#     '''
#     def __init__(self,*args):
#         super().__init__(*args)
#         self.countnum = 0
#     def __getitem__(self,pos):
#         self.countnum += 1
#         return super(CounterList,self).__getitem__(pos)

# oric = ["dsds",2,3]
# c = CounterList(oric)
# del c[0]
# print(c.countnum)
# d = c[1]+c[2]
# print(c.countnum)

# class numd(ABC):
#     def __init__(self,data):
#         super(numd,self).__init__
#         self.method = data
#     def printn(self):
#         print(self.method)

# numdd = numd("dsds")

# setattr(numdd,"method","ffff")
# print(numdd.method)
                                       
#特性 为什么要引入特性的代码
# class Rectangle:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def returnsize(self):
#         return self.a,self.b
#     def setsize(self,value):
#         self.a,self.b = value

# '''当我想要调取size信息的时候 我可以通过类中的方法来获取 但这样还是不方便 如果我们都重新设置一个属性 多次工作之后代码会显得冗长
#    最重要的是 如果我有一天需要更改我的需求 将属性调整到size 而通过方法来获取和更改a和b时 代码需要修改非常多的内容
#    因此引入特征
# '''
# #property函数实现特性定义
# class Rectangle:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def returnsize(self):
#         return self.a,self.b
#     def setsize(self,value):
#         self.a,self.b = value
#     size = property(returnsize,setsize)

# r = Rectangle(3,4)
# print(r.a,r.b,r.size) #3，4，(3,4)
#装饰器(类方法 静态方法)
# class original:
#     def shout():
#         print("hell0")
#     shout = staticmethod(shout)
#     def say(self):
#         print("my")
#     say = classmethod(say)
#这样定义的两种特殊方法也可以使用装饰器来编写
# class original:
#     @staticmethod
#     def shout():
#         print("hell0")
    
#     @classmethod
#     def say(cls):
#         print("my")
#     say = classmethod(say)
#静态方法和类方法都是可以不用实例化就调用的 静态方法中一般不会使用self 而类方法中一般会使用cls这个名字
# original.shout()
# original.say()

#如果我直接使用__getattr__之类的方法 我可以对多种属性存取情况进行一定的处理 所以相较于property更为复杂 但更为灵活
# class Rectangle:
#     def __init__(self,a=10,b=8):
#         self.a = a
#         self.b = b
#     def __setattr__(self,name,value):
#         if name=='size':
#             self.a,self.b = value
#         else:
#             self.__dict__[name] = value
#     def __getattr__(self,name):
#         if name == 'size':
#             return self.a,self.b
#         else:
#             raise TypeError("this is an error")
        
# r = Rectangle()
# print(getattr(r,'size'))
# setattr(r,'size',(20,20))
# print(getattr(r,'size'))

#迭代器定义方法 迭代器的作用就是在一些情况下替代列表等 因为列表会一次读入所有的数据
# class listsample:
#     def __init__(self,a=0,b=1):
#         self.a = a
#         self.b = b
#         pass
#     '''只要存在__next__和__iter__这两个特殊方法的时候 这个类就是一个迭代器'''
#     def __next__(self):
#         self.a,self.b = self.b,(self.a+self.b)
#         #if not self.b>100:return self.b zh这句话不能起到暂停的作用
#         if self.b>100: raise StopIteration #这句很重要
#         return self.b
    
#     def __iter__(self):
#         return self
    
# l = listsample()
# print(next(l)) #1
# print(next(l)) #2
# #此时这个迭代器就可以被正常读取
# for i in l: #这里不写range()
#     print(i)

#再尝试刚才编写列表协议的部分：
# class CounterList:
#     def __init__(self,begin=0,step=2):
#         self.begin = begin
#         self.step = step
#         self.ownlist = {}
#         pass
#     def __setitem__(self,pos,value):
#         self.ownlist[pos] = value
#     def __getitem__(self,pos):
#         if pos<1000:
#             try:
#                 return self.ownlist[pos]
#             except KeyError:
#                 return self.begin+self.step*pos
#         else:
#             raise StopIteration #这里去写StopIteration也是可以的
         
# couterlist = CounterList()
# for i in couterlist:
#     print(i)

# class Counterlist(list):
#     def __init__(self,*args):
#         super(Counterlist,self).__init__(*args)
#         self.countnum = 0
#     def __getitem__(self,pos):
#         super(Counterlist,self).__getitem__(pos)
#         self.countnum += 1

# counter = Counterlist("such")
# for i in counter:
#     print(i) 


#生成器定义方法 生成器就是特殊的迭代器 只不过每一次next()或者是send()每一次都会将yield后面的值给到生成器中 所以要注意这个独特的运行方式

# def SimpleCoder(x):
#     '''一个无限循环的生成器'''
#     while True:
#         data = yield x  #如果不是外部send进去的数据，x= yield y这样的写法 一定是None 所以才会无限循环
#         if not data==None:
#             break

# sim = SimpleCoder(10)
# print(next(sim))
# print(next(sim))  
# print(next(sim))  
# print(next(sim))  

#一个说明上述运行逻辑的例子
# def SimpleSeq():
#     for i in range(5):
#         y = yield i
#         print("输出send送入的值",y)

# sim = SimpleSeq()

# print("输出yield生成的第一个值",next(sim))
# print("输出yield生成的第二个值",sim.send(10))


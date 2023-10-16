from string import Template
from math import e
from math import pi
from copy import deepcopy
from math import sqrt

# edward = ['men', 13]
# john = ['woman', 17]
# name = [edward, john]
# print(name)
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num1 = num[:]
# if(num==num1):print("True")
# print(1 in num)
# num2 = num[:]
# num[0] = 10 
# print(num2)
# sentense = "hello, im a %s, and my %s is a nurse"
# value = ("student", "mom")
# print(sentense%value)

# sentense1 = Template("hello, im a $a, and my $b is a nurse")
# sentense1.substitute(a="student", b="mom")
# print(sentense1.substitute(a="student", b="mom")) #直接写sentense1输出的不是字符串

# print("{2} {1} {3} {0} {2} {1}".format("not", "be" ,"to", "or"))

# print("{name} is {value}".format(name="pai",value=pi))
# print(f"Euler's constant is {e}")

# total_width = int(input("Please input width: "))

# item_width = 10
# price_width = total_width - item_width

# item_fmt = "{{:{}}}{{:>{}}}".format(item_width, price_width)
# price_fmt = "{{:{}}}{{:>{}.2f}}".format(item_width, price_width)

# print("="*total_width)

# print(item_fmt.format("Item","Price"))

# print("-"*total_width)

# print(price_fmt.format("Apple",2.465))
# print(price_fmt.format("Pinapple",3.25468))
# print(price_fmt.format("Pear",1.26565))
# print(price_fmt.format("Mango",7.37))

# print('='*total_width)

# print("my name is Ethan".center(39,"*"))

# print("$$$$dsjjalsdjlasjkdlasjdl*****$$$$44444".find("444",0,16))

# seq = ["1", "2", "3"]
# sep = "+"
# print(sep.join(seq))

# dir = "", "user", "mydesk", "doc"
# print("C:"+"\\".join(dir))

# print("THIS IS MY WAY".lower())
# print("this is my way".title())
# print("this is my way".replace("is","eez"))

# print("C:\\user\\ethan\\doc!".split("\\"))

# print("******$$$$$$$dasjkhdkashdkjsa&&&&&&".strip("*$&"))

# table = str.maketrans("cs", "kz")
# print("this is color".translate(table))

# info = [("name","Alice"), ("age",20)]
# infor = dict(info)
# infor1 = dict(name="Alice", age=20) #这里的name和age不能用引号，表示的是实参
# print(infor)
# print(infor1)

# info = {"name":"Alice", "age":20}
# print("my name is {name}, and my age is {age}".format_map(info))

# info = {"name":"ALICE","machine":["win", "macos", "linux"]}
# info1 = info.copy()
# info2 = info
# info["name"] = "johj" #这是替换值 而不是原地修改 copy复制后只有原地修改才会使得双方都发生改变 但如果是直接赋值，即info2 = info，怎么改变都是双方都发生改变
# info1["machine"].append("centos") #append就是原地修改的结果
# info3 = deepcopy(info) #deepcopy是深复制，这样的复制效果就是互不影响的
# info3["name"] = "mary"
# print(info)
# print(info1)
# print(info2)
# print(info3) 

#print(dict.fromkeys(["name", "age"],"novalue")) #创建指定键的项

#get同样重要 防止代码出错
# d = {"name":"Alice","age":20}
# print(d.get("keys","NoItem"))
#setdefault和get类似，但不同的是setdefault会增加原来没有的项
# d = {"name":"Alice","age":20}
# print(d.setdefault("gender","NoValue"))
# print(d)

#items keys values出现了一个很重要的概念，就是字典视图，它可以当成列表一样使用列表的方法，但仍然不是列表
# d = {"name":"Alice","age":20}
# ditems = d.items()
# print(len(list(ditems)))
# print(d.values())

#pop和popitem都是列表之类的pop方法
# d = {"name":"Alice","age":20}
# d_new = {"age":21}
# d.update(d_new)
# print(d)

# value = "dnjsajd"
# value1 = "dsjkhf"
# value2 = "kljfdl"
# print(value, "", value1, value2) #默认输出多项时有空格
# print(value+"-", value1, value2) #使用字符串相加就可以实现无空格间隔输出
# print(value, value1, value2, sep="-") #改变默认间隔字符
# print(value, end="") #两行输出时本来是换行符为默认间隔字符，此处也可以改成其他字符
# print(value1)

# from somemodule import function as fction 默认模块和函数加载

# x, y, z =1, 2, 3
# print(x, y, z)

# dictonary = {"name":"Alice", "age":20}
# x, y = dictonary.popitem()
# print(x,y)

# a, b, *rest = [1, 2, 3, 4]
# print(rest) #这种赋值的方法可称为序列解包 同时tuple和string也可 但使用*时赋值得到的一定是一个序列 例如以下一个例子
# x, *y, z = "xyz"
# print(x,y,z) #此时Y输出的结果是包含一个字符的list

#同时还有增加赋值和链式赋值 此部分在C和C++代码中有体现

#值得说明的是，在Python中包括普通的false None作为bool型0的输入，"" [] () {}这几个空数据结构都可以作为false的输入

#前面的转换函数包括list tuple dict bool型同样有自己的转换函数
# print(bool("dsjadlkas"))

# name = input("Input your name:")
# if name.endswith("Gumby"):
#     print("Hello! Gumby")
# else:
#     print("Hello! Stranger")

# name = input("Input your name:")
# callname = "friend" if name.endswith("Gumby") else "stranger" #作为三元运算符和C中的 A？B：C一致

# name = input("Input your name:")
# if name.endswith("Gumby"):
#    print("Hello! Gumby")
# elif name.endswith("Jacky"):
#    print("Hello! Jacky")
# else:
#    print("Hello! Stranger")

# 关于if的判断机制，有几点需要补充说明的：
# 第一点是比较运算符，总的来说有> < == >= <= 多种比较形式，但相较于C等 python还多出几种：
# print("hin" is "hin")
# a = b = [1,2,3]
# c = [1,2,3]
# print(a == c)
# print(a is c) #此处可看出两者的区别，is代表的是两个对象是不是同一个 并不是相等即可
# 比较运算符还包括 in 结合not可有 is not和 not in两种比较运算符

#比较相同类型的值时，数据结构的比较规则和C比较类似，也是比较字典序的大小，如
# print("a"<"B")
# print("a".lower()<"B".lower())

#此处介绍两个常用的函数
# print(ord(" "))
# print(chr(132523)) #输出了一个我也不知道是啥的字

#第二点是bool运算符，比较运算符的输出结果是一个Bool型值，而bool运算符本身即是以bool型变量作为运算符输入的内容
# if(1<10 and 10>1):
#     print('correct')
# if(not 0):
#     print('correct')
# if(10<1 or 10>10):
#     print('wrong')
# 还需要说明一点：bool运算符带有短路逻辑的特点，也即如果前一个判断不对不符合条件，他是不会看后面一半的 这在一些算法的代码中有所体现

## 有一个和if书写语法很类似的是assert 当代码中有一些必不可少的条件需要满足时 希望当条件不满足时代码即时崩溃，这比之后运行后某时崩溃要好得多，assert之后可以加上特定的报错情况
# age = -1
# assert -1 < age < 100, "age is a positive integer"

# 循环的使用可以用一个输入名字的来进行
# name = ""
# while not name or name.isspace():
#     name = input("Please input your name:")
# print(f"Hello, {name}")

# 当存在可迭代对象的循环时，经常使用的循环语句是for
# print(range(0,10)) #range(0,10)只能输出range(0,10) 类似一个遍历结果 但最终如果需要输出列表 还需进行转换 range(10)默认是从0-9
# name = "ethan xiang"
# for name_a in name:
#     print(name_a)
# name = "ethan xiang"
# for name_a in range(len(name)):
#     print(name[name_a])

#如果是字典 可以使用items或者指定要key or value
# infor = {"name":"xiang", "gender":"man"}
# for key, value in infor.items():
#     print(key, value)

# info = ["name", "xiang", "gender", "man"]
# num = [1, 2, 3, 4, 5]
# print(zip(info, num)) #直接输出的不是一个序列
# print(list(zip(info, num))) #输出的是对应项结合成tuple的序列 即使是项数不同 也只会对齐到相同项  

##值得说明的是前面讲到的字典视图，和这里的zip 再加上刚才的range(10)之类的数据 虽然不直接是序列 但都可以调用序列相关的操作

#一般来说 我们需要进行索引的情况下会这样写：
# strings = ["dsakdhas", "dsadffd", "fklfd", "mffss"]
# index = 0
# for string in strings:
#     if("a" in string):
#         string = "haha" ##这里不能写string = ”index“ string只是改变了循环当中的string变量 
#         print(string) #这句可做一个检测
#     index += 1
#     print(string)
# print(strings)

# strings = ["dsakdhas", "dsadffd", "fklfd", "mffss"]
# for index, string in enumerate(strings):
#     if "a" in string:
#         print(string)
#         strings[index] = "haha"
# print(strings)

# print(sorted([1, 3, 2, 5, 4]))
# print(sorted("dhjkfhkdjs"))#这里的两次sorted在list提到是有原因的 因为输出的内容一定是list
# #值得说明的是后面的reversed 这里输出的不是list 但可以调用序列的方法
# print(reversed("dhjkfhkdjs"))
# print(list(reversed("dhjkfhkdjs")))
# print("+".join(reversed("jlfdlsf")))

#break和continue的功能不再赘述 写算法的人应该很熟悉
#值得一说的是循环不停止的一个条件
# while True:
#     name = input("please input your name:")
#     if not name.strip():  
#         break
#     print("my name is",name)

## 需要着重说明一下序列推导 同理也会有字典推导 但没有元组推导 元组推导会变成生成器
# print([x*x for x in range(10)]) #一定需要加上[]或者{} 不然输出的东西不是数据结构
# print([x*x for x in range(10) if x%3==0])

#可以尝试编写一个时间复杂度为平方的名字匹配函数
# girls = ["alice", "bernice", "clarice"]
# boys = ["alice", "bernice", "clarice"]
# print([boy+"+"+girl for boy in boys for girl in girls if boy[0]==girl[0]])

##这样的代码时间复杂度并不理想 很好的一个改进方式可以使得时间复杂度从o(m*n)变成o(m+n)
# girls = ["alice", "bernice", "clarice"]
# boys = ["bob", "clark", "adam"]
# bestmatch = {}
# for boy in boys:
#     bestmatch.setdefault(boy[0],[]).append(boy)
# print([girl+"+"+match for girl in girls for match in bestmatch[girl[0]]])

#pass在一些代码尚未写完的地方可以做一个填充 pass本身并不带有任何语义，比如下面的这个例子
# name = input("please input your name:")
# if name=="alice":
#     print("hello alice")
# elif name=="bernice":
#     pass
# else:
#     pass

#del的运算符非常好用 这里在list中其实已经有提及，他其实可以作为序列的整体删除操作
#python代码中有这样的特性
# a = "dskda"
# b = a
# print(a,b,sep= "+")
# a = None
# print(b)
# b = None
#当没有变量名称使用这个字符串常数时 python解释器会自动的释放这部分空间 称之为垃圾收集 但我们同样能用相同的思路用del来处理
# x = "dsfdf"
# y = x
# del(x)
# print(y)
# del()只会删除当前的变量

# exec()和eval()需要谨慎使用，它是将字符串中的表达式和语句执行出来 这在一些网络应用程序中是非常危险的 
# 这里需要特别注意的是代码运行空间 否则会出现比较尴尬的错误 可以看下面这个例子
# exec("sqrt = 1")
# sqrt(100) #'int' object is not callable 原因就是刚才的赋值将原来的函数名覆盖
# scope = {}
# exec("sqrt = 1",scope)
# print(sqrt(100),scope["sqrt"])
# eval执行的是字符串中的表达式，所以在eval中我们可以设置一个读取表达式的函数，如下：
# print(eval(input("please input an expression:")))
# scope = {}
# scope["x"] = 10
# scope["y"] = 20
# print(eval("x * y",scope))
#这么能做的前提是eval会返回表达式的值
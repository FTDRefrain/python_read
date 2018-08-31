'''
1. iterator

for ?
for (int i = 0; i < i_max ; i ++)
i = 0 i= 1初始化赋值
i++ 递进 i= i + 2

通过实现下面两个魔法方法（可以用dir看对象的魔法方法）
1. iter iter(obj) obj.__iter__()
2. next next(obj) obj.__next__()

(a)
for i in range(10):
    pass


(b)
iter_obj = range(10)
iter(iter_obj)

while True:
    try:
        i = next(iter_obj)
    except StopIteration:
        break
'''
# 下面是iterator的实现
# class Pow2(object):
#     def __init__(self, max):
#         self.max = max
#         self.n = 0
#
#     def __iter__(self):
#         self.n = 0
#         不返回有错误
#         return self
#
#     def __next__(self):
#         if self.n < self.max:
#             self.n += 1
#             return 2 ** self.n
#         else:
#             raise StopIteration
#
#
# p = Pow2(10)
# for i in p:
#     print(i)

'''
2. python instance method, class method, static method
实例方法只能在实例上面调用，绑定是self
instance method a = A() a.foo() a.bar()
绑定是cls，
class method bind class
静态相当于工具方法，不希望暴露到外面
static method
'''

# class A(object):
#     @staticmethod
#     def s_foo():
#         pass
#
#     @classmethod
#     def c_foo(cls):
#         pass
#
#     def foo(self):
#         pass
#
#
# a = A()
# a.foo()
# A.c_foo()

'''
引用类型
[] {}

深拷贝 浅拷贝
使用deepcopy进行浅拷贝
from copy import deepcopy
l1 = []
l2 = deepcopy(l1)
l1.append(1)
print(l2)

l1 = [1, [1, 2], 3]
l2 = l1[:]
'''

# 因为是深拷贝，第二次调用的时候就是[1,1]
# def foo(a=[]):
#     a.append(1)
#     print(a)
#
# foo()
# foo()

'''
3. lambda closure closure ref

lambda是匿名函数
算法适配
1. algorithm sort(lambda x : x['key'])
2. map reduce filter
'''
# import functools
# import operator
# mul2 = lambda x: 2 * x
# print(mul2(3))
#
# map，将数组依次进行函数
# print(list(map(lambda x: 3 * x, [1, 2, 3, 4])))
# filter，过滤的作用
# print(list(filter(lambda x: x % 3 == 0, [1, 2, 3, 4])))
# reduce在python3里面被移除了
# print(functools.reduce(operator.add, [1, 2, 3, 4, 5], 5))

'''
closure
闭包：通过返回函数，在调用返回，使得内部函数可以访问外面的变量
带来的问题就是，函数是调用的时候再去找的，这样原来的外部变量可能
就不是之前想要的值
通过设置默认值，就会将之前的结果拷贝，避免这个问题；
'''

# def greeting(msg):
#     def hello(name):
#         print(msg, name)
#     return hello
#
# h = greeting("welcome")
# h("akira")

# l = []
# for i in range(10):
#     def _(i=i):
#         print(i)
#     l.append(_)
#
# for f in l:
#     f()

'''
4. args kwargs
args打包成tuple
kwargs打包成dict
*args  a,b,c,d
**kwargs k = v
'''

# def log(*args, **kwargs):
#     print("args", args)
#     print("kwargs", kwargs)
#
#
# log(1, 2, 3, 4)
# log(1, 2, [1, 2, 3], c=4)

'''
5.
起源于：希望所有python的人实现同一个方法的时候采用同样的策略 
list comprehension
[i for i in range(10)]
dict comprehension
{k:1 for k in range(10)}
list generator
(i for i in range(10))
dict generator
filter method，就是后面通过if进行条件的过滤
'''

'''
6. decorator
AOP aspect oriential programming
类似调试或是其他功能，上线的时候不想显示出来
通过AOP的思想将这些东西拿掉
if debug:
    xxx
else:
    yyy
'''

# def simple_wrapper(fn):
#     def _():
#         #print(fn.__name__)
#         return fn()
#     要返回这个函数
#     return _
#
# 对于单参数
# def fix_arg_wrapper(fn):
#     def _(x):
#         #print(fn.__name__)
#         return fn(x)
#     return _
#
# 问题是很难处理带有默认值的函数
# 使用已经有的库


# def all_args_wrapper(fn):
#     def _(*args, **kwargs):
#         print(*args, **kwargs)
#         return fn(*args, **kwargs)
#     return _
#
# 装饰器特有的声明方式
# @simple_wrapper
# def foo():
#     pass
#
# @all_args_wrapper
# def bar(a, b, c):
#     pass
#
# #foo()
# bar(1, 2, 3)

'''
7. magic method
__xxx__

每一次访问类变量的时候会进行的操作
__getattribute__
每一次存变量的时候进行的操作，python3里面移除了
__setattribute__

当类里面不存在的时候，就会访问getattr的方法
__getattr__
不存在，且本身带有赋值操作的时候，访问的是setattr
__setattr__

专业名称是
missing method
'''


# class LogAll(object):
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#         self.c = 3
#     def __getattribute__(self, item):
#         print(item)
#
# l = LogAll()
# print(l.a)
# l.a = 1
# l.b
# l.c

# class Any(object):
#     def __getattr__(self, item):
#         print(item)
#
#     def __setattr__(self, key, value):
#         print("set", key, value)
#
# a = Any()
# a.a
# a.a = 1

# class Any(object):
#     def __getattr__(self, item):
#         def _(*args, **kwargs):
#             print("function name", item)
#             print("args", args)
#             print("kwargs", kwargs)
#
        # 设置了之后，再次访问的时候就有这个函数了
#         setattr(self, item, _)
#
#         return _
#
#
# a = Any()
# a.fuck(1, 2, 3)
# a.shit(1, 2, [1, 2, 3], c=[])

'''
8. mixin
c, c++, java

循环引用的问题
b -> a
a -> b

a -> a interface
b -> b interface

b->a interface
a->b interface

python里
mixin
这样A也可以访问B的内容而不需要进行引用
Final(A,B,C)
'''


# class A(object):
#     def foo(self):
#         print("foo")
#     def bar(self):
#         print("bar")
#         self.shit()
#
# class B(object):
#     def shit(self):
#         print("shit")
#
# class C(A, B):
#     pass
#
# c = C()
# c.bar()

'''
protocol
rpc
JSONRPC

client
    server_client server_client.attack(xxx)
---->
Server
    logic.attack(xxx)

rpyc
'''


# RPC设计
'''
1. tcp server tcp client
    tcp server 的方法
    bind accept recv parse call
    tcp client 的方法
    connect send data
2. function name function args function kwargs

核心在于
将服务端的程序写到客户端里面，然后客户端直接调用，一旦调用的时候
采用__getattr__的方法，
由于本身客户端是没有这些方法的，可__getattt__能访问不存在的方法并调用
魔法方法的设置，所以实现了向服务端发送JSON的功能
将方法名字和参数传输到服务端，然后服务端再调用
这就是一个简单的RPC服务，减少了服务端的压力

client
    server_client server_client.attack(xxx)
---->
Server
    logic.attack(xxx)
    
使用JSON进行内容的传输 
    
    json
    {
        'function_name':name,
        'function_args':args,
        'function_kwargs':kwargs
    }
3. client
    c.foo(1, 2, 3)

    send
    {
        'function_name':'foo',
        'function_args':(1,2,3),
        'function_kwargs':{}
    }

    __getattr__ pack

4. server
    1. recv json
    {
        'function_name':'foo',
        'function_args':(1,2,3),
        'function_kwargs':{}
    }

    getattr(self, 'foo')
    getattr(self, 'foo')(*args, **kwargs)

服务端采用参数，执行对应的函数

'''

'''
vagrant

问题：开发和布测试的环境不一样

DevOps
虚拟化 虚拟机 实现即开发又测试
1. openstack（虚拟机）
2. docker（容器化测试，快）
3. vagrant 开发测试，统一开发环境（虚拟机）
'''

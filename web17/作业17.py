# 作业一：
# 写一个 set 的类, 无序且元素不重复，内部使用数组来存储元素，具有以下成员函数
# 1. remove ，删除元素
# 2. add， 增加元素
# 3. has，判断元素是否存在
# 形式如下：
# class Set(object)：
#     def __init__(self, *args)
#         self.data = []
#         # ...
#     def remove(self, x):
#         pass
#     def add(self, x):
#         pass
#     def has(self, x):
#         pass
#
#
# 作业二：
# 在作业一的基础上，在Set类里增加 __repr__  和 __eq__ 两个成员函数。
# 并通过附带 testSet() 函数的测试。
# 形式如下：
# class Set(object)：
#     # ...
#     def __init__(self, *args)
#         self.data = []
#
#     def __repr__(self):
#         pass
#
#     def __eq__(self, other):
#         pass
#
#     def remove(self, x):
#         pass
#     def add(self, x):
#         pass
#     def has(self, x):
#         pass
#
# def testSet():
#     a = Set(1, 2, 2, 3, 4, 4)
#     b = Set(1, 2, 2, 3, 4)
#     c = Set(1, 3, 4, 2)
#     d = Set(2, 3)
#     assert (str(a) == '{1, 2, 3, 4}')
#     print(a, b, c, d)
#     assert (a == b)
#     assert (a == c)
#     assert (a != d)
#     assert (a.has(1) == True)
#     a.remove(1)
#     assert (a.has(1) == False)
#     a.add(1)
#     assert (a.has(1) == True)
#
#
# 作业三：
# 参考第17课板书 hash_table 的代码，写一个类 Set，实现时间复杂度为O(1) 的 add,remove 函数 。
# 形式如下：
# class Set(object):
#     # ...
#     def add(self, x):
#         pass
#
#     def remove(self, x):
#         pass

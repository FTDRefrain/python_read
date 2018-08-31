'''
操作系统
1. 内存管理
2. 驱动管理
3. 进程线程协程
4. 文件系统

1. 内存
32位电脑 4G（最大使用内存）
DOS 内存是程序自己控制（没有进行隔离，数个程序互相访问）
Windows 统一的内存空间 4G（任何程序开都是4G）
虚拟存储器
1. CPU n核心  ALU（加法器，计算单元） cpu寄存器（给ALU数据，最快）
只进行存储和取出使用DMA(从外接设备直接导入到内存中)也行，不经过寄存器
2. 每个核心都有自己的缓存 L1 L2（不同级别，大，慢但是便宜）
不断的换缓存，有可能存在cache miss的问题
3. 整个CPu L3 3M
4. 内存 很大很大8G
5. 硬盘
6. 网络传输

虚拟存储器，统一的内存模型
一个程序 4G 内存+硬盘
电脑4G
a 1G -> 内存中  页表（通过map将虚拟地址和真实地址一一对应）
b 1G -> 内存中  页表

c 3G -> 把a存储（内存不够，将不需要的内容放到硬盘位置里面），把c load进来

a => page fault（即内存中没有找到映射）
=> page load => 正常运行
''''''
操作系统
1. 内存管理
2. 驱动管理
3. 进程线程协程
4. 文件系统

1. 内存
32位电脑 4G
DOS 内存是程序自己控制
Windows 统一的内存空间 4G
虚拟存储器
1. CPU n核心  ALU cpu寄存器
2. 每个核心 L1 L2 cache miss
3. 整个CPu L3 3M
4. 内存 很大很大8G
5. 硬盘
6. 网络传输

虚拟存储器，统一的内存模型
一个程序 4G 内存+硬盘
电脑4G
a 1G -> 内存中  页表
b 1G -> 内存中  页表

c 3G -> 把a存储，把c load进来

a => page fault => page load => 正常运行

2. 驱动(对硬件层进行了封装)
    ps/2 usb bluetooth
    flopy（python运行其他内容的驱动包） disk
    linux: 统一成文件(驱动写成文件) read write seek（实现这些端口基本可以搞定）
3. 文件系统
    使用数组存起来文件的地址，之后直接找这个数据就行)
    [meta元信息 对应的文件位置（偏移量） 对应的文件大小]
    格式化： 会把所有信息抹掉
    快速格式化：meta清空

    所有的文件路径，存在同一个file
    /main/main.py -> file load -> execute
'''

'''
1. 进程（操作系统资源分配的最小单位） 
pid 时间片（在很短的时间运行程序的一小部分，多个时间片组织起来就搞定了多进程）
2. 多线程（就像pycharm中一边下载一边调页面）
3. 线程和进程
    进程间通信 pipe file socket（中转，慢）
    线程通信 n线程来说 我都可以看到进程中的全局数据

    对于一个进程来说，你持有了一个页表
    对于同一个进程内的线程，你共享同一张页表
4. 多线程同步问题

    数组 支持add
    1. 把数组size + 1
    2. 把add的这个数字放在 data[size]

    两个线程 同时add
    1. A线程 走了1
    2. B线程 也走了1
    3. A存了数据 data[size] = xxx
    4. B也存了数据 data[size] = xxx
    有可能产生A没有存进去数据，而且数组倒数第二位不清楚

    核心在于（两个步骤不影响的话，多线程没有问题）
    你的操作被拆分（分不清谁先谁后）
    解决方案呢？
    1. atomic swap_and_cmp
    2. 加锁，mutex，信号量，读写锁，自旋锁。

    加锁以后，我对这个资源有所有权，
    在我所有操作没有结束前，
    其他操作这个数据的人，就要等待

    数组 支持add
    1. 加锁
    2. 把数组size + 1
    3. 把add的这个数字放在 data[size]
    4. 解锁

    两个线程 同时add
    1. A线程 走了1
    2. B线程 也走了1
    3. A 2
    4. A 3
    5. A 解锁
    4. b走2，3，4

    同步会有问题？产生了死锁
    哲学家进餐

    1. 为什么死锁？获取资源的顺序不一样
    对于底下哲学家 先1后2
    对于上面哲学家 先2后1
    这样A找2的时候要等，B找1的时候也要等，产生了死锁
    
    解决方法：
    所有的哲学家都是先1后2
    1. 调整最后一个人的顺序
    2. 如果我那不到右手，那我左手的也不要

    线程安全的交换数据的函数
    swap(a,b)
    a.lock()
    b.lock()
    exchange(a.data, b.data)
    a.unlock()
    b.unlock()
    
    上面的不是安全的，例子如下
    swap(a,b) ------ swap(b,a)
    
    id(a) id(b)，不去判定的话，获取资源顺序不一样，一旦给一个调序的使用
    就会产生死锁

    Python? GIL global interpreter lock（自带的多线程锁）
    可能使本身多线程的能力废掉？
    计算的话，使用CPU，不会提高，
    IO的话，使用内存会提高一点

    并发 并行
    不管你多少个线程，只要你系统能处理多个事情（一小段时间内），就是并发的
    并行 这些事情都是在同一时间（及其精准的同一时刻）执行的 多线程 多进程

    同步异步 
    同步：事件发生与否，需要你自己去检查（自己不断访问）
    异步：事件的发生与否，这个是别人通知给你的
    
    阻塞非阻塞（遇到事情的时候）
    阻塞 等
    不等，就是非阻塞（检测是否可以调用，这时候就是同步和异步的问题了）
'''

'''
编译 解释 JIT
编译？ 一个代码编译成另外一种代码，编译到机器码，目标代码就是机器码
因为不同机器架构不同，所以要编译后机器才能懂
解释？ c语言是统一的，那我用c语言写出一个虚拟机，这个机器是可以部署到任何机器的
     python语言，语言逐条转换成对应的虚拟机指令，然后就可以跨平台使用
JIT just in time compiler 混合式
把最热的代码替换成编译到机器码

动态VS静态
a = ''
a = 1
a = True

a = ''
a = 'hello'
a = 'test'

强类型弱类型
1 + '1'
1 + 1

有GC 无GC garbage collection
没有GC的：new delete // malloc free C和C++里面的处理方式
有gc: java golang python ruby scala js
new
1. mark & sweep 
concurrent mark sweep（JAVA里面的通过并发解决）
通过标记，之后不断的扫，代价高，扫的时间长
2. ref counting
对ref进行计数标记，

python实现方式
1. ref counting
2. mark & sweep（类似）

a b
a.parent = b
b.child = a
形成了循环引用，大规模的引用导致GC实现不了

weakref
弱引用，解决了上述的循环引用的问题
'''

'''
python高级技巧
1. generator
2. iterator
3. class method, instance method, static method
4. lambda closure（闭包）
5. *args **kwargs
6. magic method
7. list comprehension
8. dict comprehension
9. decorator
10.默认参数
'''

'''
1. generator
for i in range(1000000000)
for i in xrange(100000000)[python2的写法]

l = [1...1000000000]
for i in l:
    print(i)
因为一个循环占了很大的空间
希望1就够了
'''
# 整个就是一个generator

def my_range(n):
    i = 0
    while i != n:
        i += 1
        # yield进行了中止操作,很关键的
        yield i


r = my_range(10)
for i in r:
    print(i)



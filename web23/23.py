'''
1. vagrant（有UI版本）
vagrant init --->
改产生的文件内容，vm.box里面改成自己设定的名字
vagrant up
vagrant ssh 进行登录
suspend halt 暂停和终止
package 打包

    openstack（虚拟化）
    docker（容器）
2. 架构（architecture）
web application
复制整体然后向新机器里面布置，问题就是登陆，注册等小业务也要复制
SOA 面向服务编程（因为登录，验证这类服务可以直接抽出来，其他一起用）
micro service
    2.1 不同服务tcp 语言的异构（大量IO和大量计算也就是费CPU的需求语言不同）
    2.2 数据接口api（返回的不是html而是类似JSON的数据），
        前端渲染，前后端渲染混合（看本身静态和动态内容的分工）
    2.3 自动弹性，容器，虚拟化，LaaS PaaS
        直接使用docker，将微服务直接复制然后部署
3. 分布式
CAP猜想->CAP定理（下面三个最多同时存在两个）
C 一致性，不同的人访问的时候产生相同的结果
A 可用性，每个人对反应的时间容忍度不一样
P 网络分区的可容忍性，
当一台机子挂掉，要么停止访问，要么从另一边拿到不完整的数据
服务器挂掉的问题不能避免，所以要考虑C和A的问题
    3.1. 小米（排队等手机，牺牲可用性拿到了一致性）
    3.2. 电商 做秒杀（本身只有1个，但是上三个或者根本就是随便上的，差的补出去就好）
    3.3. 存在有的公司，为了CA的存在，自己去杀网络分区


4. 后端现有架构图
放在了笔记里面
5. jsonrpc ? xmlrpc? soap ? restful api?
jsonrpc
使用http协议进行传输
传输的是json，收到的也是json
结果里面有一段的result['result']
js使用jsonrpc jquery直接去git上面或是谷歌找

xmlrpc http xml
soap，没用了

restful api http method
可以使用http的method去做CRUD，但是灵活度不够
这个和jsonrpc是现在的主流

6. 性能的代价
jsonrpc ? 缺点
 6.1 overhead，http带来的问题，头部太大
 6.2 单工（http一应一答，socket本身可以复数监听）
         好处
 6.3 简单
 6.4 乱序（TCP做不到按顺序进行访问，http可以）

 tcp 双工？
7. websocket js socket socket-io
原生websocket
onopen, onclose, send, onmessage
外部包
socket-io
windows上面有编译不了的东西，直接去找binary（编译好的包）

8. 聊天室
1. 聊天，room，对于room广播
2. 加入房间，退出房间
3. jquery，页面DOM的操作
4. socket.io
5. socket.io server
6. tcp socket io 问题就是没有session这些http的东西


'''
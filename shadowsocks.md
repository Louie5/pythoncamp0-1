#Ubuntu下shadowsocks科学上网姿势

###步骤  

1. 安装shadowsocks-qt5  
经过测试，可能人品问题我用其他shadowssocks版本均失败，shadowsocks-qt5是可视化的一个版本，可用。 

**友情提示：在apt-get这类指令中，习惯性加sudo，保证你有足够权限执行命令**
> sudo add-apt-repository ppa:hzwhuang/ss-qt5  （找软件）
> sudo apt-get update  （更新你的软件库）
> sudo apt-get install shadowsocks-qt5

 2 . 配置客户端  
按供应商提供的账户信息配置好，如果信息正确，就会启动成功。杂项里头可以配置：设置成功自动启动。
![](http://i.imgur.com/tpPDQcG.jpg)

 3 . 配置浏览器  
> 1. 在windows和mac下都不用配置，直接使用系统默认就好。
>  ![](http://i.imgur.com/gfeCFQS.png)  
> 如果chrome浏览器据说还有一个swichysharp插件可以用,不知道可不可以用到firefox上。  
> 2. 我使用的是firefox，打开【连接设置】。  
> 3. 一定选择要使用【手动配置代理】~~~啊多么痛的领悟悟悟悟  
> 4. 默认有个http代理127.0.0.1，这个一定要清空。 ~~~啊多么痛的领悟悟悟悟  
> 5. socks主机为socks5，地址和端口如图所填。

###说明：
> 1. 在mac和windows下，可以使用pac模式，也就是在pac文件中设置哪些地址需要翻墙，不在列表内的地址就直连。
> 2. 在ubuntu下默认是全局模式，也就是一律走代理翻，浏览器访问墙内的速度慢点。  
> 3. 当然我们也可以自己写pac，在浏览器设置中选择自动代理配置。不过貌似不能直接将windows下的搬过来。
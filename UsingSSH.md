##初用SSH##

本文所测试使用的操作系统平台：WindowsXP windows7 Ubuntu14.04

**+ 提纲**

**- 为什么要使用 SSH**

- 我遇到什么问题了？
- 这是什么原因？
- 找到了什么解决办法？

**- 怎么用 SSH**

- 如何理解 SSH？
- 生成 SSH 公钥秘钥？
- 在 GitHub 和本地进行配置
- 使用 SSH 协议进行操作
- 试错之路

----------------------------------------------

**+ 为什么要使用 SSH**

-  从本地 Git 连接 GitHub ，最简单的是使用 https 协议

> $git remote add learning https://github.com/rosing/learning/learningpython.git 
   
 > 上面这条语句将通过https协议建立一个名叫 learning 的连接，通常情况下我们可能在网上资料上看到的是 origin 。另见：关于 origin 的理解。
 
> $git push -u learning +master  

> 使用上面这条语句，将把本地 Hit 库的文件推到 GitHub 数据库，用的当然就是 https 协议

- 现在问题来了
 - [X] 每次取推数据都要输入账号密码，好麻烦。
 - [X] 默认windows XP 不支持 https 协议 。 
 
  > 【第一次试错】从系统提示得知，系统文件 libcurl.dll 不支持 https 协议，从网上下载了一个支持https 协议的 libcurl.dll ，遭遇本机注册失败，需要修改注册表。由于 libcurl.dll 是Windows系统运行的重要文件，由系统自动产生，不应轻易改动，加上修改注册表太危险，本次操作放弃。

- SSH挺身而出，能够解决上面两大问题

**+ 怎么用 SSH**

- 理解SSH  
SSH 是一种远程传输协议 [1] ，简单来说好处有两个，一个是安全，一个是方便，配置好文件后不用每次输账号密码。ps：有时候使用某项技术的时候只需要简单粗暴理解就够了。^-^

- 生成公钥秘钥 [2]  
>$ssh-keygen -t rsa -C "462507545@qq.com"   
  
>系统将生成 .ssh 文件夹，下面有两个秘钥，默认名字就不改了。同一级有个.config 文件，用来配（keng）置(die) ssh 。  
>
【第二次试错】在 Windows 下安装 git bash 选用的是支持 command line ，也就是可以在 windows 的 cmd 命令框中直接使用 git命令，经测试 cmd 框执行效率高过 bash 。我在cmd下执行 ssh-keygen 却提示外部命令，改到打开 bash 窗口执行，通过。

- 去 GitHub 配置秘钥  

  > 把位于 .ssh 文件下的后缀为 .pub 的文件用文本编辑器打开，复制里头那一堆看不懂的数字。  
  > 到 GitHub 上找到 SSH 配置的地方，输入这一堆数字，保存。  
  
- 测试 
>$ssh -T git@github.com    

> 看到Hi rosing! You've successfully authenticated, but GitHub does not provide shell access. 你就知道 ssh 配置基本成功了（我后面还是有问题*_*）。我账号是 rosing，你看到的可能是 Hi your-github-account 。  
> 
【第三次试错】俺自作聪明把指令中的 git@github.com 改成 rosing@github.com 结果返回钥匙不匹配。 以下省去试错血泪文3000字，耗时30分钟。直接输入上述指令，运行通过。

- 使用SSH协议进行操作  
 > 【第四次试错】 建立连接：$git remote add sshtest git@github.com:rosing/learningpython.git  
系统返回错误信息：fatal:Not a git repository(or any of the parent directories):.git.   
>
- 我以为数据库写错，经查，需要在当前的 git 的工作目录下才能建立连接（半夜脑子都糊了*_*） ，但是如果连接已经建好，则在任何目录下 pull push 都没问题，这个已经建好的连接保存在本地的一个文件里，因此关机时有效的，除非手动 remove 这个连接。  
- 但试错的过程中，参照错了一个资料（保持脑子清醒是多重要），修改了.gitcongfig文件，导致以下错误返回：fatal:bad config file line 5 in c:/user/Administrator/.gitconfig.   


    >以下都是错的，完全不用写到. gitconfig里头去哈  
    >Host git  
    >HostName github.com  
    >PreferredAuthentications publickey    
    >IdentityFile ~/.ssh/github_rsa   

>事实上这个 .gitconfig 文件在这个应用下是不需要修改的，就一行，啥也别改。


**结语**

- 本地 Git 与 GitHub 数据传输支持两种协议形式，https 和 SSH。  

- 采用 SSH 协议是为了解决 https 的麻烦同时兼顾更高的安全性。

- SSH协议与平台无关，Windows Ubuntu Mac 皆同。

- 它需要生成和配置秘钥文件，同时到 GitHub 进行设置。  

- 它与远程 GitHub 的连接在写法上与 https 协议略有不同，但 push pull clone 等操作语法不受协议影响。  

- 如果确实觉得 SSH 复杂的，使用默认的 https 协议也是一样的，毕竟也不是说麻烦到不能用。






**参考文献**

1. SSH（安全外壳协议）： http://baike.baidu.com/link?url=8gUH1KKAHUuUEC7GrRV159bHQwP4fgn4IOhupgVYJfoT_z5oOkQfBAE_nVfyv8jlH5j_ipGCxxA_-4vDrD-cN1DBotLrPrtmHZi7Di8Pe2e
2. 创建SSH密钥，并连接 GitHub : http://www.blogways.net/blog/2013/04/10/generating-ssh-keys-4-github.html
3. 生成ssh ： http://blog.csdn.net/hustpzb/article/details/8230454

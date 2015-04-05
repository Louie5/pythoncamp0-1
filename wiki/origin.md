#理解Origin#

###**Origin 在哪里看到？**###

和大家一样，我第一次看到 origin 是在命令 git add remote origin https://github.com/myname/myrepository.git 中。它基本上在 remote、push 和 pull 相关语句中出现。

###**Origin 是个啥？**###

根据官方帮助资料显示（使用 git --help 得到的相关帮助文件）。    

这个 origin 是 「 a remote name for the repository from the current branch 」  

而各大百度谷歌查阅到的解释基本是：默认远程仓库，默认服务器，默认分支名。 

把这个 add 过程称为「添加远程库」   

各种疑惑丛生！

###**问题来了**###

- 本地库是 git ，远程库难道不是 github 吗？怎么能在这里建？
- 服务器不是在 github 上吗，我能随便创建服务器？
- 如果是分支名，为嘛找遍 github 整个站点找不到一个叫做 origin 的默认分支，master 倒是一直都在？
- 为什么我建立了一个 origin 后，不能再用这个名字了？重启电脑也不行啊。难道我已经失去了默认分支了？

###**真相**###

origin 实际上可以理解为**连接通道的名字**，相当于给你建立的传输通道取个名字，这样好方便push pull 等文件传输。

好比我们要喝水，总得要找根吸管，为这根吸管取个名字，比如redstraw, bluestraw ，这样每次去喝就知道用这哪吸管喝水了。

###**进一步理解**###

问题一：连接名可以重复吗？  
>答：不可以。同一台电脑上，已经存在有某个名字的连接，就不能再 add 了。所以大家看到想再建一个名叫 origin 的连接，系统会报错。

问题二：可以为同一个数据库创建多个不同名字的连接吗？  
>答：可以。这样的话，我们无论通过哪一个连接名，得到的结果都是一样，虽然是多此一举，但并没有错。
这类似咱们往同一个杯子里放了好几根吸管，无论从哪根吸管喝，喝的都是同一杯。

问题三：不同的终端建的连接，名字可以重复吗？  
>答：是的。这个连接保存在本机 config 文件里。 比如我有两台电脑，这两台电脑上可以有同名的连接，比如都叫 origin 或者 都叫 lovepython。 以此推测，这个连接在电脑重新启动后，不会消失，除非手动删除。 

问题四：我怎么看我的连接？  
>答：命令 git remote 或者 git remote -v 。后者可以看到连接到的远程数据库

问题五：如何删除连接？  
>答：命令 git remote remove name 。原有的连接删除后，它的名字将可以重新被使用。
  

###**参考资料**###

1. 本机自带help文件。
2. git remote的用法 http://blog.csdn.net/wangjia55/article/details/8802490
3. git push：http://www.yiibai.com/git/git_push.html
4. 添加远程库：http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013752340242354807e192f02a44359908df8a5643103a000
#双推github gitbook

操作系统：Ubutu

以本次作业pythoncamp0为例

**设置github**

1. 注册github
2. fork一个repository，得到自己的一个git仓库实例https://github.com/rosing/pythoncamp0.git

**关联gitbook**

1. 用github账号进去gitbook
2. 新建一本book，取个心爱的书名和文件名，保存后出现这个界面，选择Link to GitHub![](http://i.imgur.com/HJKVhte.jpg)

3. 在这里填上你要关联的那个repository，记得是自己fork的那个，别填上人家的了![](http://i.imgur.com/R9bEEG5.jpg)
4. 下拉屏幕，点击左下角(坑爹的地方，害我找好久)的保存。
5. 这就关联好了。你去编辑book的时候，会发现pythoncamp0上面的东西已经跑到你的book上来了，如果你在这里编辑保存，github上也会同步。

**从终端推**

1. 在Ubuntu上安装git库程序，默认貌似没有，自带的软件中心有，搜一下就找到了。

2. 终端运行  git int   注释：这算是初始化git库一下

3. （可选）终端运行  git clone https://github.com/rosing/pythoncamp0.git /home/lgp/mygit/pythoncamp0   注释：这段命令将github上面那个pythoncamp0.git库复制到你指定的本地文件夹

4. 如果你不打算复制到这个库本地也没关系，可以跳过第三步

5. git add mygit/pythoncamp0 注释：把你本地文件夹里的东东文件加到工作区

6. git commit -m "my first pythoncamp0 commit" 注释：这算是放到缓冲区，等待上传

7. git remote add origin https://github.com/rosing/pythoncamp0.git 注释：这里创建一个连接，主机名是orgin，可以自定义（坑爹，我以前以为是关键字），不能重名。git remote 不带任何参数，可以看你的所有主机。

8. git push -u origin +master 这里有一个+号，要是木有加号，系统可能会报错“更新被拒绝，因为您当前分支的最新提交落后于其对应的远程分支。” +号是强推，原来代码界也喜欢强行啊啊啊。



至此，你会发现你本地的文件已经推到了github，可喜的是你gitbook上关联的数据也已经更新。

**写此文档，纪念我折腾的血泪史**

**祝你成功，么么哒**
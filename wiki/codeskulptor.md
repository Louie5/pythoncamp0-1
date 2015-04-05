#Ubuntu下本地模拟运行Codeskulptor

###准备工作  
感谢政府，我们要科学上网，教程见 https://github.com/rosing/pythoncamp0/blob/master/shadowsocks.md  

**友情提示**  
1. 养成sudo的习惯  
2. 大小写敏感

###开始安装  

1. 更新pip  
1) sudo pip install --upgrade pip  
2. 安装依赖包  
2) sudo pip install PySDL2  
3) sudo pip install mercurial  
4) sudo pip install SimpleGUICS2Pygame
3. 安装 pygame 开发环境  
5) sudo apt-get build-dep python-pygame  
（上面这一句好像也可以用 sudo apt-get install python-pygame代替）  
6) sudo apt-get install python-dev  
4. 抓pygame源文件  
7) hg clone https://bitbucket.org/pygame/pygame
5. 安装pygame  
8) cd pygame  
9) python setup.py build  
10) sudo python setup.py install  

###开始使用
将在codeskulptor 的代码本地保存为一个.py的文件，将

import simplegui  
改为：  
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui    

在命令行中运行本地脚本  
python test.py  

然后就能在本地操作codeskulptor 上的游戏了。就不用连到服务器操作。
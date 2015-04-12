#windows环境下本地化下Codeskulptor

1. 下载并安装git bash  
  + 地址：http://git-scm.com/download/win
2. 打开bash输入pip install PySDL2
  + 注意：windows是木有sudo一说的，所以，你懂的
3. pip install SimpleGUICS2Pygame
4. 下载并安装pygame for windows   
  + 地址：http://www.pygame.org/download.shtml

可以在python程序中引用了  
import SimpleGUICS2Pygame.simpleguipygame as simplegui  

###本地与codeskulptor运行的小区别
- 在codeskulpotor上支持u'中文'这种方式为变量赋值计算等，本地不支持，本地需要在第一行注明支持的字符类型：# -*- coding: utf8 -*-
- 即使做了上一步，本地运行simplegui对象的中文部分会出现乱码，但不至于报错
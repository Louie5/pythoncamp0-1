##学习使用 DISQUS##

**背景**  

在跟开智小伙伴聊到 kindle 的时候，第一次听说了 DISQUS，得知这是一个第三方的留言系统，主要用于支持别人在自己网站上进行留言评论。 在当晚大妈的第一次 Q&A ，我再次听到它。我觉得是时候安装并学习使用DISQUS，让导师和组员看到我的任务完成情况，并提出宝贵的意见。

**开始之旅**  

开始总是从搜索引擎开始，输入关键字后，找到官网，一看，全英文，为了节约时间，我找到一个中文教程[1]。 
  
- 官网注册账号  
- 配置：它会问你想在什么网站使用，名字是什么，URL是什么，所属类别是什么。  
- 
【问题一】：它让我选择一个 platform 平台，可选的内容分别是Universal Code、Wordpress、Blogger、Tumblr、Squarespace、TypePad、MovableType、Drupal、Joomla，可我连上面这些是什么并不清楚，我以为会有一个GitBook的选项，看来我可能理解有误。  
*解决过程*：

1. 查资料得知，platform是指目标网站源码类型，可GitBook应该选啥呢？组合一些关键字搜索，无果。我选了第一个Universal Code，跳出一个页面，是一些插入到网站的代码，姿势可能不对，暂时搁置。 
2. 引出第二个尝试，去下载一个可安装的插件。 找到一个npm insall 。npm 是啥？
3. npm 是 安装 nodejs 依赖包。 nodejs又是啥？
4. nodejs 是一个基于Chrome JavaScript运行时建立的平台。是不是又要找到它的windows安装包？先搁置一下。我去试试第一步。
5. 把之前disqus网站上提供的代码拷贝到gitbook的readme当中，为了防止刷新不及时问题再次出现影响判断，稍微做了一点手脚。果然又是只能刷新到 edit ，不能刷新到read。
6. 去github看看，找到文件后打开，并没有出现期待的评论页面，而是“Please enable JavaScript to view the comments powered by Disqus.”
7. 由于源文件是md，我估计可能是不支持md内置javascript，特意做了一个html文件传上去，其中内置有简单javascript代码，看是否能解释html。结果显示的是html源代码，我以为是代码转化过，但网页后缀是html，下载到本地也是一个html文件，并且可以正常运行。第六步可以不纠缠了。不知道github是如何不转换代码而让浏览器直接显示源码的。会不会是因为https的关系？目测可能性极低。这又是一个盲点。待解。
8. 这时候回去看gitbook，已刷新，可以看到它是支持html语法的。但为嘛该出现的评论框没有呢？是js的问题吗？我决定写一段简单js代码。
9. 问题找到了，系统将js代码中的引号进行了转义。推测这是为了系统安全，要知道直接运行js太危险了。那么问题又回到了第一步。我不能使用 Universal Code 这种方式。  
 
【问题二】官网上找不到适合window的下载包，事实上，其他系统的也没看到。  

#终于
**找到了一个靠谱的做法**  

1 修改gitbook书根目录下的book.json文件  

{  
	"plugins":[  
		"disqus"  
	],  
	"pluginsConfig":{  
		"shortName":"rosinggitbook"  
	}  

}  


2 在disqus网站添加信任域  
位置：setting - advanced - Trusted Domains  
填入：gitbook.com,gitbook.io







**参考资料**  
1. wordpress 如何使用评论插件 Disqus http://jingyan.baidu.com/article/ff42efa919f1b8c19f220245.html
2. Gitbook 的插件支持 http://www.wosoni.com/wosoniblog-berlinix-article-details-40424091.html  
3. JavaScript configuration variables
  https://help.disqus.com/customer/portal/articles/472098-javascript-configuration-variables

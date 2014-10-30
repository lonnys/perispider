==========运行环境及运行方法===========
美女网站爬虫代码
1、安装scrapy
pip install Scrapy
2、在本项目根目录中执行下面指令即可爬取图片URL
scrapy crwal peripic
3、调试方法如：
scrapy shell http://www.22mm.cc/mm/qingliang/
===========新建项目========
1、创建项目
scrapy startproject <项目名>
2、初始化项目
cd <项目名>
scrapy genspider <爬虫项目名> <爬虫域名>

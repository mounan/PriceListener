
本次使用的工具🔧

* Python 3.7 +
* BeautifulSoup4 [官方文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)
* Google Chrome浏览器
* VSCode代码编辑器



### Python 环境配置

电脑里还没有python3.7以上环境的同学，可以点击[anaconda官网](https://www.anaconda.com/products/individual#Downloads)，找到合适自己系统的版本，按照指示下载安装就可以了。

安装好之后打开terminal或者cmd，输入python，回车，出现类似下面的信息则说明安装成功。

![スクリーンショット 2020-12-28 15.18.06](/Users/zmn/Library/Application Support/typora-user-images/スクリーンショット 2020-12-28 15.18.06.png)



### BeautifulSoup配置

打开teminal（mac）或者cmd（win），输入```pip install beautifulsoup4```回车即可。



### 安装VSCode

这里使用的是vscode编辑代码，大家可以使用自己喜欢的编辑器。

打开[官网](https://code.visualstudio.com/download)，选择适合自己的版本下载安装即可。



###基本思路

做一个网络爬虫不断爬取メルカリ上用条件检索得到的所有PS5商品，再按价格排序，通过字符串解析获取最低价位的几个商品，将他们的价格和链接保存到json文件里实时刷新并显示出来。

<img src="/Users/zmn/Library/Application Support/typora-user-images/スクリーンショット 2020-12-26 2.09.55.png" alt="スクリーンショット 2020-12-26 2.09.55" style="zoom:50%;" />

​							当前最低价位的4个PS5的价格和链接



### 完整代码

先上完整代码截图

![スクリーンショット 2020-12-28 16.26.36](/Users/zmn/Library/Application Support/typora-user-images/スクリーンショット 2020-12-28 16.26.36.png)

![スクリーンショット 2020-12-28 16.27.00](/Users/zmn/Library/Application Support/typora-user-images/スクリーンショット 2020-12-28 16.27.00.png)

代码文件我放在了github里，有兴趣的小伙伴可以clone一下，有关git的用法以后我也会单独写一篇文章介绍。

代码中有些地方是可以自己调整的：

* 第26行是检索价格范围，当前为5W～8W，如果要搜索6w到10w以内的就把范围改成（60000,10000）

* 第32行是不希望标题和描述信息中含有的词汇列表，这里因为不想买数字版的，所以我加入了关于数字版的词汇（'デジタル', 'digital', 'Digital', 'CFI-1000B01', 'Degital', 'デシダル', 'ディスクドライブ非搭載'），你也可以自己添加词汇，这个方法可以有效筛掉一些没用的商品信息。
* 第34行是希望标题和描述信息中含有的词汇，你可以添加一些你想要的商品一定会含有的词汇，可以有效筛选出目标商品的信息。

* 剩下的代码大家可以不需要更改，有兴趣的可以仔细看一下，我就不赘述了。

## Get Music Lists Information

####  文件一览

* python程序文件
  1. main.py : 接口，调用文件该文件可完成相关功能
  2. web_get.py:  爬取网页内容并保存
  3. print_img.py ：生成数据图表
  4. word_cloud.py ：生成词云
* 其他
  1. .jpg文件皆用于生成词云
* 生成文件
  1. 两个后缀为csv的歌单列表文件
  2. 十一个后缀为png的数据可视化图片文件
  3. 四个后缀为txt的中间文本文档

####  代码方法及类

1. main.py ：main函数，程序调用接口

2. web_get.py:  

   * tag类：标签内容保存

   * Data类：爬取+网页解析+内容保存

     方法：write_data_csv，write_data_txt，getin_pages，get_cbox，get_sbox，get_moreinfo，get_tags，get_desc

     （具体功能详见代码文件）

   * get_infor()：调用该文件的接口

3. print_img.py ：生成数据图表

   * 方法：print1、print2、print3、print4

     绘制不同数据图

   * 方法：select、depart、link

     数据处理

   * 方法：mixprint3，mixprint4

     调用接口

4. word_cloud.py ：生成词云

   * Cloud类：词云类

   * 方法：makeclouds

     调用接口


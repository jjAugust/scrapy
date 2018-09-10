#! /bin/sh                                                                                                                                            

export PATH=$PATH:/usr/local/bin

cd /home/junjie/junjie\ xiong/gitcode/scrapy/taobao/taobao/spiders

nohup scrapy crawl taobao -a url="https://traveldetail.fliggy.com/item.htm?spm=a1z10.5-b-s.w4011-15573120551.30.1ac82654sOVXmQ&id=545656466491&rn=d97248afb97dfe662da9e87837aa80bd&abbucket=7" -a wantprice=2100 -a para0=1 -a para1=8 -a para2=1 -a para3=4 -a para4=2 -o result.json
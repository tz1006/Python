#!/bin/sh

# yum -y update

yum -y install sqlite-devel

# 安装Twisted依赖
wget -P /home/build https://twistedmatrix.com/Releases/Twisted/16.4/Twisted-16.4.1.tar.bz2
tar -xjvf Twisted-16.4.1.tar.bz2 -C /home/build
# cd /home/build/Twisted-16.4.1
python /home/build//Twisted-16.4.1/setup.py install

# pip安装 scrapy
pip install scrapy

# 删除安装包
rm -f /home/build/Twisted-16.4.1.tar.bz2
rm -rf /home/build/Twisted-16.4.1

# http://www.tokyjiao.com/archives/214

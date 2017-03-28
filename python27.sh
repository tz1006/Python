#!/bin/sh

# yum -y update
# 备份并卸载默认python
yum -y install xz gcc openssl-devel
mv /usr/bin/python /usr/bin/python2.6.6
sed -i '1c #!/usr/bin/python2.6.6' /usr/bin/yum

# 下载python27
wget --no-check-certificate -P /home/build https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tar.xz
tar xf /home/build/Python-2.7.13.tar.xz -C /home/build
cd /home/build/Python-2.7.13

# 编译安装
./configure --prefix=/usr
make && make install
cd /root

# 安装pip
wget --no-check-certificate -P /home/build https://bootstrap.pypa.io/get-pip.py
python /home/build/get-pip.py
rm -f /home/build/get-pip.py

# rm -f /root/Python-2.7.13.tar.xz
# rm -rf /root/Python-2.7.13

# http://www.jianshu.com/p/a633a7070a24
# https://ruter.github.io/2015/12/03/Update-python/

# IPTV m3u 直播源 收集 & 汇总

 [项目详细说明](https://evilcult.dev/07/19/2019/IPTV-Projects/)

 [项目更新记录](https://evilcult.dev/tags/iptv-m3u-maker/)

## 简介
---
### 主要功能
收集网络上现有的一些网友共享的直播源, 将其汇总后.

对每个连接进行测试, 同时记录当前网络对该连接的延迟, 同时对其标题进行一定的格式化.

最终, 针对当前网络生成一份可用的, 同类速度最优的 “播放列表”.

将其输出为 **m3u** 文件

程序内置服务器功能, 本地运行访问: http://{你的IP}:9527/m3u

### 目前进度

目前库存频道总数: 1024

已放出优质频道总是: 269

**!!! 项目持续更新中 !!!**


## 数据来源
---
- https://www.jianshu.com/p/2499255c7e79
- V2ex - [Dotpy](https://www.v2ex.com/member/Dotpy) 提供1600+可用播放源
- http://iptv807.com/

*数据源总是挂掉的比新增的快,欢迎推荐稳定数据源*


## 项目使用方法
---
本项目基于 **python3.7** 进行开发

### 手动执行
```
git clone https://github.com/EvilCult/iptv-m3u-maker.git

cd iptv-m3u-maker/python

python iptv.py
```
### 人生苦短, 我用Docker 

建议以[Docker](https://www.docker.com/) 的方式,直接在路由器上运行,本地检测地址访问,更为精准.

```
git clone https://github.com/EvilCult/iptv-m3u-maker.git

cd iptv-m3u-maker

docker build -t iptv-maker:latest .

docker run -it -d --name iptv -p 9527:9527 iptv-maker:latest
```
*build的过程中会自动配置程序运行环境, 其中已包含flask服务器,可直接访问 ' http://{运行docker的机器的IP地址}:9527 ' 查看当前程序状态,以及相关操作*

### 其他

**待程序稍微稳定**后回只做一个镜像丢到docker hub上去, 直接拉取就好.

## 其他
---
### 相关项目
~~「[iptv-m3u-player](https://github.com/EvilCult/iptv-m3u-player)」 - 基于本项目的衍生项目, 基于Electron+React编写的一个轻量级桌面客户端.频道数据会随本项目更新. Mac上不知道用什么客户端的,可以试试.~~ (当前更新涉及文件路径修改, 该项目暂时不可直接使用.)

Android TV 请使用 [Kodi](https://kodi.tv/ ) + ‘PVR IPTV Simple Client’

iOS 请使用 Cloud Stream

PC 我就不太了解了....

### 已知问题
- 访问速度慢,视频卡顿
  - 解决方案: 不要直接引用项目中的tv.m3u8文件,clone项目到本地,在本地网络环境下执行项目,生成新的文件
- 电视,广播未分开
  - 暂时未处理,会v在后续版本进行分类
- 程序运行报错 
  - 可能是部分 分享源 网站服务当机... 可自行注释部分代码 or 提交 [issues](https://github.com/EvilCult/iptv-m3u-maker/issues)
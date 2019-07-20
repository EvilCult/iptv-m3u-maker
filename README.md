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

### 目前进度

目前库存频道总数: 2269

已放出优质频道总是: 563

**!!! 项目持续更新中 !!!**


## 数据来源
---
- https://www.jianshu.com/p/2499255c7e79
- https://github.com/billy21/Tvlist-awesome-m3u-m3u8
- V2ex - [Dotpy](https://www.v2ex.com/member/Dotpy) 提供1600+可用播放源
- https://www.sheng521.top/zyfx/zbyfx

更多来源还在考虑要不要加入....


## 项目使用方法
---
本项目基于 **python3.7** 进行开发

```
git clone https://github.com/EvilCult/iptv-m3u-maker.git
cd iptv-m3u-maker
python main.py
```
人生苦短, 我用Docker 

建议以[Docker](https://www.docker.com/) 的方式,直接在路由器上运行,本地检测地址访问,更为精准.

两行命令构建运行环境
```
docker pull python:3.7
docker run -it --name python3 -v {脚本所在滤镜}:{容器里随便你想要的路径} python:3.7
```

## 其他
---
### 相关项目
「[iptv-m3u-player](https://github.com/EvilCult/iptv-m3u-player)」 - 基于本项目的衍生项目, 基于Electron+React编写的一个轻量级桌面客户端.频道数据会随本项目更新.
Mac上不知道用什么客户端的,可以试试.

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
# IPTV 直播源 收集&汇总项目

#### 简介
---
主要功能是收集现有大佬发布的直播源m3u8文件

测试是否好用,并记录该源的访问延迟. 同时按一定规则格式化该源的标题.

最后程序会在同类的源中选出延迟最低的一个,按频道优先级汇总,并输出一个m3u文件.

目前库存频道总数: 2269

已放出优质频道总是: 563

**!!!这个项目的代码还在进行中!!!**


#### 使用方法
---
项目根目录执行
```
python main.py
```
即可

建议以docker的方式,直接在路由器上运行,本地检测地址访问,更为精准.

#### 相关项目
「[iptv-m3u-player](https://github.com/EvilCult/iptv-m3u-player)」
基于本项目的衍生项目, 基于Electron+React编写的一个轻量级桌面客户端.频道数据会随本项目更新.

Android TV上有Kodi, iOS上有Cloud Stream, PC/Mac上不知道用什么客户端的,可以试试这个:[iptv-m3u-player](https://github.com/EvilCult/iptv-m3u-player)


#### 已知问题
- 访问速度慢,视频卡顿
  - 解决方案: 不要直接引用项目中的tv.m3u8文件,clone项目到本地,在本地网络环境下执行项目,生成新的文件
- 电视,广播未分开
  - 暂时未处理,会v在后续版本进行分类

#### 目前资料来源
---
- https://www.jianshu.com/p/2499255c7e79
- https://github.com/billy21/Tvlist-awesome-m3u-m3u8
- V2ex - [Dotpy](https://www.v2ex.com/member/Dotpy) 提供1600+可用播放源
- https://www.sheng521.top/zyfx/zbyfx
- 第五个源还在考虑要不要加....

#### 运行环境
---
**python3.7**
人生苦短,我用Docker,本脚本,开发&运行&测试环境均使用docker镜像完成


两行命令构建
```
docker pull python:3.7
docker run -it --name python3 -v {脚本所在滤镜}:{容器里随便你想要的路径} python:3.7
```

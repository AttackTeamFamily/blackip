# 黑IP收集(攻击向)
### 项目简介
在日益增强的攻防对抗中，全网测绘、云沙箱、动态样本分析等等防御项的系统对TeamServer展开了疯狂围剿。此项目旨在收集整理这些IP用于对抗分析。

### 数据
|ACL|Blocked IP|Line Num|File Size|description
| :---: | :---: | :---: | :---: | :---: |
|blackip.txt|238745164|1556|22k|黑ip合集|
|sandbox.txt|65343|320|4.4k|云沙箱|
|redwarden_ip.txt|238744726|1143|16k|RedWarden项目收集|
|cs_scan_ip.txt|206|206|2k|扫描CobaltStrike的恶意IP合集|
### 使用
```
git clone https://github.com/AttackTeamFamily/blackip.git
cd blackip
bash start.sh
```

### 贡献说明
希望公鸡队小伙伴们，积极贡献ip。贡献方式：
- 提交Issues
- 提交格式：
```
简介：全网测绘ip|云沙箱ip|漏扫ip|......
IP列表：
1.1.1.1/24
2.2.2.2
3.3.3.3
```
- 量大可以直接上传压缩包
### 贡献致谢
- [@timwhitez](https://github.com/timwhitez)
- [RedWarden项目](https://github.com/mgeeky/RedWarden/edit/master/data/banned_ips.txt)
- [@Winck](https://github.com/By-Winck)
- [@waterrr](https://github.com/waterrr/BlackIP/blob/main/ip.txt)

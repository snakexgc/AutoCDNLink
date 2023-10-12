# AutoCDNLink
帮助你快速生成套CF优选域名的CDN节点，减少自己手动输入优选域名的麻烦。
# 说明
本项目不存在偷节点信息的情况，因为是一个纯本地项目！源码全在 [main.py](https://github.com/snakexgc/AutoCDNLink/blob/main/main.py) 中，用chatgpt生成，理论上纯shit，无任何营养。
# 文件说明
- AutoCDNLink.exe 主程序
- domaindx.txt 电信联通优选域名 （这里的优选仅仅只是指非采用cloudflare ip的优选域名）
- domainyd.txt 移动优选域名 （支持去重，去重后顺序会发生变化，不影响使用，懒得修了）
- source.txt 你的初始节点（可同时放入多个节点）
- dx.txt 套上电信联通优选域名的节点存放在这里，每次运行程序会自动清空，无需手动清空
- yd.txt 套上移动优选域名的节点存放在这里，每次运行程序会自动清空，无需手动清空
# 如何使用？
## 1. 源码运行
克隆源码到本地，填好一下信息
```
domaindx.txt 电信联通优选域名 （这里的优选仅仅只是指非采用cloudflare ip的优选域名）
domainyd.txt 移动优选域名 （支持去重，去重后顺序会发生变化，不影响使用，懒得修了）
source.txt 你的初始节点（可同时放入多个节点）
```
执行main.py即可
## 2. 打包程序执行
和上面基本一样，只是需要将AutoCDNLink.exe和
```
domaindx.txt 电信联通优选域名 （这里的优选仅仅只是指非采用cloudflare ip的优选域名）
domainyd.txt 移动优选域名 （支持去重，去重后顺序会发生变化，不影响使用，懒得修了）
source.txt 你的初始节点（可同时放入多个节点）
```
这三个文件放到同一目录下，填好信息后运行主程序即可。

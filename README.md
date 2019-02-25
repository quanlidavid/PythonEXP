Python 的学习笔记
====
## 环境相关
[Python 安装](https://pythonguidecn.readthedocs.io/zh/latest/starting/install3/osx.html)

[iTerm2 + oh my zsh](https://www.jianshu.com/p/9c3439cc3bdb)

Sublime + MarkdownEditing + Markdown preview + LiveReload + Sublimerge + Pretty Json

[Python最佳实践指南](https://pythonguidecn.readthedocs.io/zh/latest/)

[virtualenv使用](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)

pycharm新建项目的时候可以选择新建virtualenv:
然后导出依赖包文件
```pip freeze > requirements.txt  ```
“freeze” the current state of the environment packages

[git里加入需要忽略的文件](https://github.com/github/gitignore/blob/master/Python.gitignore)
把idea的文件也忽略掉：.idea/

拉取代码后可以:
新建项目的project interpreter，然后装依赖的包
```pip install -r requirements.txt```
install the same packages using the same versions

## 语法相关

### 基本语法
```python
print("abc")
print(5+3)
print("abc"+"efg")
print("abc"*8)
print("abc\n"*8)
```

## Django

## 项目相关

## 学习资料
1. [笨办法学 Python](https://learnpythonthehardway.org/python3/preface.html)
2. [Python 基础教程](http://www.runoob.com/python/python-tutorial.html)

## 快捷键
Python Console
+ ^+p: 上一个命令
+ ^+n: 下一个命令
PyCharm
+ ⌘>:  光标挪到行尾
+ ⌥ ⌘ V: 新建变量

## Cheat Sheet
[Python 3 Cheat Sheet](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf)
[Python 3 – Quick Reference Card](https://www.cs.put.poznan.pl/csobaniec/software/python/py-qrc.html)
[Python3 in one pic](https://github.com/coodict/python3-in-one-pic/blob/master/README.md)
[Python 运算符](http://www.runoob.com/python/python-operators.html)
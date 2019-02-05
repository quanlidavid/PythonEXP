Python 的学习笔记
====
## 环境相关
Sublime + MarkdownEditing + Markdown preview + LiveReload

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

## Reference: 《Flask Web 开发》

## Environment

Python 3

Mac OSX

## Introductory Chapter: 安装

1.安装第三方工具 virtualenv

```
sudo easy_install virtualenv
```

显示其版本信息：

```
virtualenv --version
```

```
sh-3.2# virtualenv --version
15.1.0
```

2.git clone 文件夹用以保存代码：

```
git clone https://github.com/miguelgrinberg/flasky.git

cd flasky

git checkout 1a
```

3.在flasky中创建虚拟环境venv

```
virtualenv venv
```

```
sh-3.2# virtualenv venv
New python executable in /Users/wasdns/Desktop/flasky/venv/bin/python
Installing setuptools, pip, wheel...done.
sh-3.2# ls
.git		LICENSE		hello.py
.gitignore	README.md	venv
```

4.激活虚拟环境：

```
source venv/bin/activate
```

系统自动修改命令行提示符，加入环境名：

```
(venv) sh-3.2# 
```

5.ps.如果想回到全局环境，执行：

```
deactivate
```

6.在虚拟环境中安装Flask：

```
pip install flask
```

检验：在python界面中导入flask模块。

```
(venv) sh-3.2# python
Python 2.7.10 (default, Oct 23 2015, 19:19:21) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import flask
>>> 
```

成功安装Flask。

> 2017/2/14
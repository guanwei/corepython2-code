## 语句和语法

- 井号（#）表示之后的字符为Python注释；
- 换行（\n）是标准的行分隔符（通常一个语句一行）；
- 反斜线（\）继续上一行；
- 分号（；）将两个语句连接在一行中；
- 冒号（：）将代码块的头和体分开；
- 语句（代码块）用缩进块的方式体现；
- 不同的缩进深度分隔不同的代码块；
- Python文件以模块的形式组织。

## 变量赋值

### 赋值操作符

```
anInt = -12
```

### 增量赋值

```
x = x + 1
x += 1
```

### 多重赋值

```
x = y = z = 1
```

### “多元”赋值

```
x, y, z = 1, 2, 'a string'
(x, y, z) = (1, 2, 'a string')
```

## 标识符

### 专用下划线标识符

- _xxx    不用‘from module import *’导入
- _xxx_   系统定义名字
- _xxx    类中的私有变量名

## 基本风格指南

### 模块结构和布局

1 起始行（Unix）
  ```
  #/usr/bin/env python
  ```
2 模块文档
  ```
  "this is a test module"
  ```
3 模块导入
  ```
  import sys
  import os
  ```
4 变量定义
  ```
  debug = True
  ```
5 类定义
  ```
  class FooClass(object):
      "Foo class"
      pass
  ```
6 函数定义
  ```
  def test():
      "test function"
      foo = FooClass()
      if debug:
          print 'ran test()'
  ```
7 主程序
  ```
  if __name__ == '__main__':
      test()
  ```
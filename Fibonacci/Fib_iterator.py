# -*- coding: utf-8 -*-
"""
  实现斐波那契数列
   方法二：迭代器
"""

class Fibonacci(object):       #定义类

    def __init__(self, n):     #初始化
        self.n = n             #n为生成数列的项数
        self.current = 0       #保存当前生成的数据列的第几个数据，元素初始化个数为0
        self.a = 0
        self.b = 1             # 两个初始值

    def __next__(self):        #当调用next()函数时，可获取下个数
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a      #返回值
        else:
            raise StopIteration    #抛出异常，一旦执行了raise语句，raise后面的语句将不再执行

    def __iter__(self):         #迭代器的__iter__ 返回自身即可
        return self

if __name__ == '__main__':
    while 1:
        print("**********请输入要打印的斐波拉契数列项数n的值***********")
        n = input("enter:")
        if not n.isdigit():
            print("请输入一个正整数！")
            continue
        n = int(n)
        fib = Fibonacci(n)
        for i in fib:
            print(i)
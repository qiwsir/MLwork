# -*- coding: utf-8 -*-
"""
实现斐波那契数列
"""
import numpy as np

"""
方法一：生成器
"""

def Fib_yield_while(max):
    a, b = 0, 1                #设置初始值
    while max > 0:
        a, b = b, a + b
    max -= 1
    yield a                    #执行yield函数

def Fib_yield_for(n):
    a, b = 0, 1
    for _ in range(n):          #循环遍历n次
        a, b = b, a + b
        yield a    

if __name__ == "__main__":

    while 1:
        print("**********请输入要打印的斐波拉契数列项数n的值***********")
        n = input("enter:")      #输入要计算的项数n
        if not n.isdigit():      #判断输入值是否为数字
            print("请输入一个正整数！")
            continue
        n = int(n)
        for i in Fib_yield_for(n):
            print(i)


"""
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

"""
方法三：矩阵
"""

def Fibonacci_Matrix_tool(n):
    Matrix = np.matrix("1 1;1 0", dtype ='int64')        # 使用矩阵计算斐波那契数列，改变为64位整数类型
    return np.linalg.matrix_power(Matrix, n)            # 返回matrix类型,其中np.linalg.matrix_power（）为矩阵幂乘运算

def Fibonacci_Matrix(n):
    result_list = []
    for i in range(n):
        result_list.append(np.array(Fibonacci_Matrix_tool(i))[0][0])
    return result_list

if __name__ == '__main__':
    while 1:
        print("**********请输入要打印的斐波拉契数列项数n的值***********")
        n = input("enter:")
        if not n.isdigit():            #判断输入值是否符合要求
            print("请输入一个正整数！")
            continue
        n = int(n)
        fib = Fibonacci_Matrix(n)       # 调用
        for num in fib:
            print(num)


"""
方法四：循环语句  
"""
a = 0                   #确定初始值
b = 1
num = []
print("**********请输入要打印的斐波拉契数列项数n的值***********")
n = input("enter:")     #输入想计算的项数n

while b >= 1:
    try:                #设置异常，若输入非正整数退出
        n = int(n)
    except ValueError:
        print("输入错误，请输入正整数")
        exit()
    num.append(b)
    a,b = b,a+b
    if len(num) == n:
        print(num[n-1])
        break

"""
方法五：递归
"""

def Fib_list(n) :
  if n == 1 or n == 2 :                        #n为项数，若为1、2时，结果返回为1
    return 1
  else :
    m = Fib_list(n - 1) + Fib_list(n - 2)      #其他情况下，结果返回前两项之和
    return m
if __name__ == '__main__':
    while 1:
        print("**********请输入要打印的斐波拉契数列项数n的值***********")
        n = input("enter:")
        if not n.isdigit():
            print("请输入一个正整数！")
            continue
        n = int(n)
        list2 = [0]
        tmp = 1
        while (tmp <= n):
            list2.append(Fib_list(tmp))
            tmp += 1
        print(list2)


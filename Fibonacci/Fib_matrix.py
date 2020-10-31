# -*- coding: utf-8 -*-
"""
  实现斐波那契数列
   方法三：矩阵
"""
import numpy as np

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

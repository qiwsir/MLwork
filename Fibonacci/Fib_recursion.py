# -*- coding: utf-8 -*-
"""
  实现斐波那契数列
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
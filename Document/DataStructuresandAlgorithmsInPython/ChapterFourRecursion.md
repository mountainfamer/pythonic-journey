第４章　递归
递归可以代替循环，递归可以用来表示一个函数在执行的时候调用一次或多次自身，或数据结构依赖于更小的与自身相同的数据结构；
递归不只可以表述函数功能，还可以表述自然界的现象，如俄罗斯套娃等；　
当一个函数使用递归调用时，调用将被挂起，直到递归调用结束；　
递归是学习数据结构和算法的重要技术，递归示例：
4.1.1 阶乘
阶乘的数学表示：n! = n.(n-1).(n-2)...3.2.1 (n>=1)   n!=1 (n=0)
阶乘的正规化表示形式：n! = n*(n-1)!         (n>=1)   n!=1 (n=0)
阶乘的函数表示：
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)   #没有循环出现，取而代之的是嵌套的递归调用；　
4.1.2 递归绘制英尺（english ruler）：
def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + str(tick_label)
    print(line)
def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)
def draw_ruler(num_inches, major_length):
    draw_line(major_length, str(0) )
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))
4.1.3 二分法查找
在一个排好序的列表中查找目标对象；　mid为查找是的中间序号，low与high分别为第一个和最后一个序号；　
查找时，设，mid = (low+high)/2
则：
如果查找对象在data[mid]，则一次就可以找到目标；　
如果被查找的目标<data[mid]，则递归或循环在列表前半节数据中找，查找的区间为low-(mid-1)；
如果被查找的目标>data[mid]，则递归或循环在列表后半节数据中找,查找的区间为(mid＋1)-high；
二分查找的常规函数表示：
def binary_serach(data, target, low, high):
"""
如果找到目标数据则返回真，data已排序列表，target为被查找数据，low与high指定要查找的区间；　
"""
    if low > high:
        return False
    else:
        mid = (low + high) / 2
        if taget == data[mid]:
           return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)
4.1.4 文件系统
文件系统有一个顶层的目录，其下包含文件和其他目录，目录下又有其他的文件和目录；　
文件系统的拷贝，删除操作就需要用到递归算法；　计算所有文件和目录占（嵌套）用的磁盘空间，也会用到递归算法；
算法伪代码：
DiskUsage(path):
    Input: 	要统计占用磁盘空间的路径
    Output:　　	路径下文件或目录累计占用的磁盘空间
    total = size(path)  #路径直接占用的磁盘空间
    if path就目录 then:
        for 遍历路径目录　do:
            total = total + DiskUsage(子路径)
    return total
Python代码表示：
import os
def disk_usage(path):
    total = os.path.getsize(path)    #计算path直接占用空间；　
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage（childpath）    
    return total
    
4.3 递归算法性能分析
递归算法的不同使用方法，对应的发费，效率，成本差别很大；　
如：　使用递归计算Fibonacci数列：
def bad_fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <=1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)
    
def good_fibonacci(n):
   """Return pair of Fibonacci numbers, F(n) and F(n-1)."""
   if n <=1:
       return (n,0)
   else:
       (a, b) = good_fibonacci(n-1)
       return (a+b, a)
4.4 递归的优化使用
根据递归调用的次数，可以把递归分为：
线性递归：递归函数体内最多一次递归调用；good_fibonacci就是线性递归的实例；　
二次递归：当函数内包含两次递归调用时，就是二次递归；　
多次递归；
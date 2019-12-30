#1.打印1000以内3的倍数
# for x in range(3, 1000, 3):
#     print(x)

#2.从大到小排列
# for x in range(5, 0, -1):
#     print(x)

#3.去除重复数字
#conding:utf-8
# l1 = [5, 4, 3, 2, 1, 3, 2, 2,]
# l2 = list(set(l1))
# print (l2)

# 从大到小排列
# l2.sort(reverse=True)
# print(l2)

#4.反转字符串
# a = 'ithema'
# print(a[::-1])

#5.去除重复数字并保持原来的顺序
# l1 = [1, 2, 3, 2, 4, 5, 6, 3]
# l2 = list(set(l1))
# l2.sort(key=l1.index)
# print(l2)

#6.对数组进行切片vscode有问题(它包含了结束位置)
# list = range(10)
# print(list[0:])

#7.打乱排好的数字
# import random
# alist = [1, 2, 3, 4, 5]
# random.shuffle(alist)
# print(alist)

#8.
# arr = [1, 35, 23, 17, 19, 21, 4, -4]

# def bubble_sort(arr):
#     n = len(arr)
#     for j in range(0, n - 1):
#         for i in range(0, n - 1 - j):
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]


# bubble_sort(arr)
# print(arr)  

# import qrcode
# img = qrcode.make('Some data here')

#9.给小花的信
#conding:utf-8
# print('亲爱的小花'.encode('utf-8'))

# @Time    : 2018/12/3 16:30
# @Author  : Jennings
# @Email   : zjn@wiwi.ink


def swap(x, i, j):
    """
    交换x的i，j位置元素
    :param x:
    :param i:
    :param j:
    :return:
    """
    temp = x[i]
    x[i] = x[j]
    x[j] = temp

# 选择排序

def selectionSort(x):
    i = 0
    while i < len(x) - 1:
        minindex = i
        j = i + 1
        while j < len(x):
            if x[minindex] > x[j]:
                minindex = j
            j += 1
        if minindex != i:
            swap(x, i, minindex)
        i += 1
    return x


# print(selectionSort([1, 4, 5, 3, 2, 6]))

# 二元选择排序法（选择排序改进）

def selectionSort_1(x):
    i = 0
    while i <= len(x) // 2:
        minindex = i
        maxindex = i
        j = i + 1
        while j < len(x) - i:
            if x[minindex] > x[j]:
                minindex = j
            if x[maxindex] < x[j]:
                maxindex = j
            j += 1
        if x[minindex] == x[maxindex]:
            return x
        if minindex != i:
            swap(x, i, minindex)
        if maxindex != len(x) - 1 - i:
            if maxindex != i:
                swap(x, len(x) - 1 - i, maxindex)
            else:
                swap(x, len(x) - 1 - i, minindex)
        i += 1
    return x


# print(selectionSort_1([1, 4, 5, 3, 2, 6]))

# 冒泡排序

def BubbleSort(x):
    j = len(x) - 1
    while j > 0:
        i = 0
        while i < j:
            if x[i] > x[i + 1]:
                swap(x, i, i+1)
            i += 1
        j -= 1
    return x


# print(BubbleSort([1, 4, 5, 3, 2, 6]))

# 冒泡排序法改进

def BubbleSort_1(x):
    j = len(x) - 1
    while j > 0:
        flag = False
        i = 0
        while i < j:
            if x[i] > x[i + 1]:
                swap(x, i, i+1)
                flag = True
            i += 1
        if not flag:
            return x
        j -= 1
    return x


# print(BubbleSort_1([1, 4, 5, 3, 2, 6]))

# 双向冒泡排序法(鸡尾酒排序法)

def BidirectionalBubbleSort(x):
    j = 0
    while j <= len(x) // 2:
        flag = False
        for i in range(j, len(x) - j - 1):
            if x[i] > x[i + 1]:
                swap(x, i, i + 1)
                flag = True
        for i in range(len(x) - 1 - j, j, -1):
            if x[i] < x[i - 1]:
                swap(x, i, i - 1)
                flag = True
        if not flag:
            return x
        j += 1

    return x


# print(BidirectionalBubbleSort([1, 4, 5, 7, 9, 2, 3, 6, 8]))

# 插入排序法

def InsertionSort(x):
    i = 1
    while i < len(x):
        j = i - 1
        item = x[i]
        while j >= 0 and item < x[j]:
            x[j + 1] = x[j]
            j -= 1
        x[j + 1] = item
        i += 1
    return x


# print(InsertionSort([1, 4, 5, 7, 9, 2, 3, 6, 8]))

# 希尔排序（插入排序改进）

def HashSort(x):
    gap = round(len(x) * 2 / 3)
    while gap > 0:
        print('gap = ', gap)
        i = gap
        while i < len(x):
            j = i - gap
            item = x[i]
            while j >= 0 and item < x[j]:
                x[j + gap] = x[j]
                j -= gap
            x[j + gap] = item
            i += 1
        gap = round(gap / 3)
    return x


print(HashSort([1, 4, 5, 7, 9, 2, 3, 6, 8]))

#Author: Jenliver
#集合

list_1 = [1, 4, 5, 6, 4]
list_1 = set(list_1)
#添加一个
list_1.add(999)
#添加多个
list_1.update([222, 333, 444])
#删除一个
list_1.remove(222)

list_2 = set([2, 5, 0, 4, 6])
list_3 = set([4, 5])
print(list_1, type(list_1))
print(list_1, list_2)

#交集
print(list_1.intersection(list_2))
print(list_1 & list_2)
#并集
print(list_1.union(list_2))
print(list_1 | list_2)
#差集,1有2没有
print(list_1.difference(list_2))
print(list_1 - list_2)
print(list_2.difference(list_1))

#对称差集，1和2都没有
print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2)

#子集
print(list_3.issubset(list_2))
#父集
print(list_1.issuperset(list_3))

#判断1和2是否有交集
print(list_1.isdisjoint(list_2))
#discard删除不存在的元素不会报错
list_2.discard("hhh")


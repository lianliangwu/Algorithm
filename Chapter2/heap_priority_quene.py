# coding=utf-8
# PRIORITY QUENE ALGORITHM
# 优先级队列是一种用来维护由一组元素构成的集合S的数据结构，这一组元素中的每一个都有一个关键字key。一个最大优先级队列支持以下操作

# INSERT（S，x） 把元素x插入集合S
# MAXIMUM（S） 返回S中具有最大关键字的元素
# EXTRACT-MAX（S） 去掉并返回S中的具有最大关键字的元素
# INCREASE-KEY（S，x，k） 将元素x的关键字的值增加到k，这里k值不能少于x的原关键字的值

# 最大优先级队列应用：分时计算机上作业调度

from heap import max_heapify

# HEAP-MAXIMUM 
def heap_maximum(A):
	return A[0]

# HEAP-EXTRACT-MAX
def heap_extract_max(A):
	return


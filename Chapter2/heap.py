# coding=utf-8
# HEAP ALGORITHM

import math

# HEAP
def partent(i):
	return int(math.floor((i-1)/2))

def left(i):
	return int(2*i+1)

def right(i):
	return int(2*i+2)

# HEAP_SIZE-set before call max_heapify
HEAP_SIZE={'A':0}

# MAX-HEAPIFY
# 输入为一个数组A和下标i，当max-heapify被调用时，我们假定LEFT（i）和RIGHT（i）为根的两颗二叉树都是最大堆，但这是A[i]可能小于其子女，max-heapify让A[i]在最大堆中"下降"
def max_heapify(A,i):
	l=left(i)
	r=right(i)
	# largest
	largest=i
	if l< HEAP_SIZE['A'] and A[l]>A[i]:
		largest=l
	if r< HEAP_SIZE['A'] and A[r]>A[largest]:
		largest=r
	# change largest
	if largest is not i:
		temp=A[i]
		A[i]=A[largest]
		A[largest]=temp
		# recurse
		max_heapify(A,largest)

# BUILD-MAX-HEAP
# 将一个数组A[1..n]变成一个最大堆，子数组A[( |_n/2_| )..n]中的元素都是树中的叶子，BUILD-MAX-HEAP对树中的每一个其他节点都调用一次MAX-HEAPIFY
def build_max_heap(A):
	HEAP_SIZE['A']=len(A)
	node=math.floor((len(A)+1)/2)-1
	while node>=0:
		max_heapify(A,int(node))
		node-=1

# HEAP-SORT
# 堆排序算法先用BUILD-MAX-HEAP构造最大堆，将最大元素A[1]与A[n]换，然后将A[1..n-1]建成最大堆，循环
def heap_sort(A):
	# BUILD-MAX-HEAP构造最大堆
	build_max_heap(A)
	end = len(A)-1
	# 循环
	while end>0:
		# 将最大元素A[1]与A[n]换
		temp=A[end]
		A[end]=A[0]
		A[0]=temp
		# 然后将A[1..n-1]建成最大堆
		HEAP_SIZE['A']=end
		max_heapify(A,0)
		# decrease
		end-=1

# TEST CASE
def test():
	A=[4,4,3,2,16,9,10,14,8,7]
	# max_heapify(A,0)
	# build_max_heap(A)
	heap_sort(A)
	print(A)


# MAIN
# RUN
test()





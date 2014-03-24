# coding=utf-8

# QUICK SORT 
# DEVIDE:A[p..r] -> A[p..q-1] A[q+1..r],make each element in A[p..q-1] is less or eaual than A[q],and each element in A[q+1..r] is above or equal than A[q]
# CONQUER:recurse QUICK SORT in A[p..q-1],A[q+1..r]

# QUICKSORT IMPLEMENT 

# QUICKSORT(A,p,r)
# 	if p< r
# 		then q <- PARTITION(A,p,r)
# 			QUICKSORT(A,p,q-1)
# 			QUICKSORT(A,q+1,r)

# PARTITION
def partition(A,p,r):
	# pivot element
	x=A[r]
	# divide
	i=p-1
	j=p
	while j<r:
		if A[j]<x:
			i+=1
			# exchange i,j
			temp=A[i]
			A[i]=A[j]
			A[j]=temp
		j+=1
	# exchange pivot element
	i+=1
	temp=A[i]
	A[i]=A[r]
	A[r]=temp
	# return q : the divide element
	return i

# QUICKSORT
def quick_sort(A,p,r):
	if p<r:
		q=partition(A,p,r)
		quick_sort(A,p,q-1)
		quick_sort(A,q+1,r)

# TESE CASE
def test():
	A=[2,8,7,1,3,5,66,44,44,44,124,6,4]
	quick_sort(A,0,len(A)-1)
	print(A)

# RUN
test()

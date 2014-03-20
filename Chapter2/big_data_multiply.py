# coding=utf-8
# Multiply big data multiply
import timeit
import math
import random

# normal 
def multiply(A,B):
	return A*B

# evolution
def multiply_e(A,B):
	str_A=str(A)
	str_B=str(B)
	sum = []
	for b in str_B:
		sum+= ['0']
		temp_sum=[] 
		for a in str_A:
			temp=list(str(int(b)*int(a)))
			temp_sum+= ['0']
			# add 
			temp_sum = add(temp_sum,temp)
		sum = add(sum,temp_sum)
	return sum

# add function-参数：被加数，加数
def add(A,B):
	# temp_sum-被加数，temp-加数
	if len(A) >= len(B):
		temp_sum = list(A)
		temp = list(B)
	else:
		temp_sum = list(B)
		temp = list(A)
	# add 存临时的和、进位、循环变量		
	carry=0
	i = len(temp_sum)
	j = len(temp)
	while i>0 and j>0:
		# 将两数对应的位以及前面的进位相加
		m=int(temp_sum[i-1])+int(temp[j-1])+carry
		if m>9:
			# carry
			carry=1
			temp_sum[i-1]=str(m%10)
			i=i-1
			j=j-1
		else:
			# no carry
			carry=0
			temp_sum[i-1]=str(m)
			i=i-1
			j=j-1
	# 如果两数长度相等，将最后一次的进位加在最前面
	if i is 0:
		if carry is 1:
			temp_sum = ['1']+temp_sum
	# 如果较大的数还剩余有位，就将最后一次的进位加入高位
	else:
		if carry is 1:
			k = int(temp_sum[i-1])+1
			temp_sum[i-1] = str(k%10)
			# 将最后一次的进位加入高位
			while i>1:
				if k>9:
					k = int(temp_sum[i-2])+1
					temp_sum[i-2]=str(k%10)
					i=i-1
				else:
					break
			if k>9:
				temp_sum=['1']+temp_sum
	return temp_sum

# test case
def test():
	# random test 500 case
	i=0
	while i<500:
		A=random.randint(1,9999)
		B=random.randint(1,9999)
		if list(str(A+B)) != add(list(str(A)),list(str(B))):
			print('add Failed')
			print(A,B)
			print(add(list(str(A)),list(str(B))))
			return
		i=i+1
	print('Info:Add Succeed')

	# random test 500 case
	i=0
	while i<500:
		A=random.randint(1,9999)
		B=random.randint(1,9999)
		if list(str(multiply(A,B))) != multiply_e(A,B):
			print('Failed!')
			print(A,B)
			print(multiply(A,B),multiply_e(A,B))
			return 
		i=i+1
	print('Info:Multiply Succeed!')
	return

# main function
def main():
	test()
	A = 8888
	B = 9999
	start = timeit.default_timer()
	print(multiply(A,B))
	time = (timeit.default_timer()-start)

	start = timeit.default_timer()
	print(multiply_e(A,B))
	time_e = (timeit.default_timer()-start)

	# test add method
	# print(add(list('275'),list('2750')))
	print(time,time_e)

# run
main()

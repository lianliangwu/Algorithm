# coding=utf-8

# PRIM ALGORITHM

# The algorithm starts with a tree consisting of a single vertex, and continuously increases its size one edge at a time, until it spans all vertices.

# 	Input: A non-empty connected weighted graph with vertices V and edges E (the weights can be negative).
# 	Initialize: Vnew = {x}, where x is an arbitrary node (starting point) from V, Enew = {}
# 	Repeat until Vnew = V:
# 		Choose an edge {u, v} with minimal weight such that u is in Vnew and v is not (if there are multiple edges with the same weight, any of them may be picked)
# 		Add v to Vnew, and {u, v} to Enew
# 	Output: Vnew and Enew describe a minimal spanning tree

# INF 
INF=9999999

# PRIM ALGORITHM
def prim(A,Vnew):
	# VILIAGE NUMBER
	num=len(A)
	# vertices [0,1,2..(n-1)]
	V=range(num)
	# Initialize: Vnew = {x}, where x is an arbitrary node (starting point) from V, Enew = {}
	if not Vnew:
		Vnew=[0]
	Enew={}
	distance=0
	# Repeat until Vnew = V:
	while len(Vnew)<num:
		# Not Vnew
		Vrest=[]
		for v in V: 
			if v not in Vnew:
				Vrest.append(v)
		print(Vnew)
		print(Vrest)
		shortest=999999
		# Choose an edge {u, v} with minimal weight such that u is in Vnew and v is not
		for u in Vnew:
			for v in Vrest:
				if A[u][v]<shortest:
					shortest=A[u][v]
					start=u
					des=v
		# Add v to Vnew, and {u, v} to Enew
		Vnew.append(des)
		Enew[start]=des
		distance+=shortest
	result={'distance':distance,'Enew':Enew}
	return result

# FIX DISTANCE MATRIX
def fix(A):
	# NON-DIRECTED GRAPH
	i=0
	while i<len(A):
		A[i][i]=0
		j=i+1
		while j<len(A):
			A[i][j]=A[j][i]
			j+=1
		i+=1
	# FIXED DISTANCE MATRIX
	return A

# ALREADY BUILDED ROAD
def setVnew(con):
	Vnew=[]
	for start,des in con.items():
		Vnew.append(start)
		Vnew.append(des)
	return Vnew

# TEST CASE
def test():
	# DISTANCE MATRIX
	A=[[0,990,692],[990,0,179],[692,179,0]]
	# CONNECTED ROAD DICTIONARY
	connected={0:1,1:2}
	# FIX DISTANCE MATRIX
	A=fix(A)
	# ALREADY BUILDED ROAD,SET Vnew
	Vnew=setVnew(connected)
	result=prim(A,Vnew)
	print('Prim Algorithm:shortest distance',result['distance'])
	print('Prim Algorithm:new road',result['Enew'])

# RUN
test()



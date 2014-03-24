# LINKED LIST

# NODE
class Node:
	def __init__(self,data=None,next=None):
		self.data=data
		self.next=next
	def __str__(self):
		return str(self.cargo)

# LINKED LIST
class LinkedList:
	# INIT
	def __init__(self):
		self.head=Node(None,None)
		self.tail=self.head
		self.size=0

	# APPEND
	def append(self,data):
		node=Node(data,None)
		if self.head.data is None:
			self.head=node
			self.tail=node
		else:
			self.tail.next=node
			self.tail=node
		self.size+=1

	# INSERT
	# INSERT data BEFORE bdata
	def insert(self,data,bdata):
		node=Node(data,None)
		prev=self.head
		# search
		# head
		if prev.data is bdata:
			node.next=self.head
			self.head=node
			self.size+=1
			return True
		# content
		while prev is not None:
			next=prev.next
			if next is not None and next.data is bdata:
				node.next=next
				prev.next=node
				self.size+=1
				return True
			else:
				prev=next
		print('error-cannot find before data')
		return False

	# REMOVE
	def remove(self,data):
		prev=self.head
		# empty linked list
		if self.size is 0:
			print('error-linked list is empty')
			return False
		# head
		if prev.data is data:
			if prev.next is None:
				# size=1
				self.head=Node(None,None)
				self.tail=self.head
			else:
				# size>1
				self.head=prev.next
			self.size-=1
			return True
		# content
		while prev is not None:
			next=prev.next
			if next is not None and data is next.data:
				# catch it
				prev.next=next.next
				self.size-=1
				return True
			prev=prev.next
		print('error-removed data is not exist in linked list')
		return False

	# TO STRING
	def to_string(self):
		result = ''
		prev=self.head

		result=result+'{'
		while prev is not None:
			if prev is not self.head:
				result=result+','
			if prev.data is not None:
				result=result+str(prev.data)
			prev=prev.next

		result=result+'}'
		return result

	# CONTAINS
	def contains(self,data):
		prev=self.head
		while prev!=None:
			if prev.data is data:
				return True
			else:
				prev=prev.next
		return False

	# INDEX OF
	def index_of(self,data):
		prev=self.head
		index=0
		while prev is not None:
			if prev.data is data:
				return index
			else:
				prev=prev.next
				index+=1
		# -1 NOT FOUND
		return -1		

	# SIZE
	def get_size(self):
		return self.size


# TEST CASE
llist=LinkedList()

llist.append(1)
llist.append(2)
llist.append(3)

print(llist.head.data)
print(llist.tail.data)
print(llist.to_string())

llist.insert(5,1)
print(llist.to_string())

llist.remove(5)
print(llist.to_string())

print(llist.get_size())
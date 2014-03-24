# STACK DATASTRUCTURE

# TOP-TOP ELEMENT INDEX
def top(S):
	return len(S)-1

# STACK-EMPTY
def stack_empty(S):
	if top(S) is -1:
		return True
	else:
		return False

# PUSH
def push(S,x):
	S.append(x)

# POP
def pop(S):
	if stack_empty(S):
		print('error-underflow')
		return
	else:
		x=S.pop()
		return x

# TEST CASE
def test():
	S=[1,2,3]
	print('STACK TOP INDEX',top(S))
	push(S,5)
	print('PUSH',S)
	pop(S)
	pop(S)
	print('POP',S)

# RUN
test()
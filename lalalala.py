import random
from secrets import FLAG
assert FLAG.startswith(b"d4rk{") and FLAG.endswith(b"}c0de")
FLAG = FLAG.lstrip(b"d4rk{")
FLAG = FLAG.rstrip(b"}c0de")
length = len(FLAG)
assert(length == 17)


A = matrix(ZZ, length - 1, length, lambda i, j: random.randint(-2^40, 2^40-1)) ##Generating a random integer matrix
x = vector(ZZ, list(FLAG)) 

b = A * x 
row = random.randint(0 , length - 2)
col = random.randint(0 , length - 1)
assert b"Y0u" in FLAG   #hint
A[row , col ] = random.randint(-2^40, 2^40-1)
print("A = " , list(A))
print("B =" ,  list(b))



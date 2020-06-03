A = [1/x for x in range(1, 10)]
B = [1**x for x in range(1, 10)]
C = [x for x in A if x % 4 == 0]
print(A)
print(B)
print(C)
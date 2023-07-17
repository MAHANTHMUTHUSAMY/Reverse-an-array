def reverse_range(A, B, C):
    if B > C or B < 0 or C >= len(A):
        return A
    while B < C:
        A[B], A[C] = A[C], A[B]
        B += 1
        C -= 1

    return A
A=list(map(int,input('A=').split()))
B=int(input('B='))
C=int(input('C='))
print(reverse_range(A,B,C))
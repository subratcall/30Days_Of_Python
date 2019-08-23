# Asking for number of integers
print('how many integers?\n')
N = int(input())
# Asking for the list
print('enter {} numbers each separated with a space'.format(N))
A = list(input().strip().split())

# storing the list in reverse
A_reversed = []
for i in range(N):
    A_reversed.append(A[N-i-1])

# joining each element with a space to print

print('Reversed: ' + ' '.join(str(i) for i in A_reversed))





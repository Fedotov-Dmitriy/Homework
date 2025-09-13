N = int(input())
a =[x for x in range(N+1)]
a[1] = 0
i = 2
while i <= N**0.5:
    if a[i] != 0:
        j = i**2
        while j <= N:
            a[j] = 0
            j  = j+i
    i = i+1
a = [x for x in a if x != 0]
print(a)
    

def fib(n):

    if n in [1,2]:
        return 1

    return (fib(n-1) + fib(n-2))
sum = 0    
for i in range(2,1000):
    if fib(i) < 4000000:
        if (fib(i)%2) == 0:
            sum += fib(i)
    else:
        break
print(sum)

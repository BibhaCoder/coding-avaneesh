n = int(input())
abc = int(input())
count = 0
print bin(n)
print bin(abc)
while n:
    n = n & (n - 1)
    count += 1
while abc:
    abc = abc & (abc - 1)
    count += 1
print count

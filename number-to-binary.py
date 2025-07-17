import sys
num = int(input())
bits = []
while num != 0:
  r = num % 2
  num = num // 2
  bits.append(r)
print bits[::-1]

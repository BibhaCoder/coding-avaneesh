x = int(input())
n = int(input())
print bin(x)

bit_count = len(bin(x)) - 2
print bit_count
abc = bit_count - n
left_mask = x >> n
print bin(left_mask)
right_mask = x << abc
print bin(right_mask)
a = left_mask | right_mask
print bin(a)

import math
limit = 100
for num in range(2, limit):
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
	if num % i == 0:
	   is_prime = False
	   break
    if is_prime:
	print (num)

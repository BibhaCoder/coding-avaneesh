user_input = int(input("Enter a number"))
left_shift = int(input("Enter shift"))
#shifts bits to the right by left_shift, each shift divides number by 2 and makes numbers to the left of shift 0
answer = user_input >> left_shift
print answer
  


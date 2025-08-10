big_string = input()
small_string = input()

count = 0
for char in big_string:
  if char == small_string:
    print char
    abcd = big_string.index(small_string)
    print abcd + 1
    
    


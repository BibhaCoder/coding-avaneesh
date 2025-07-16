user_input1 = input("Enter a string")
for char in user_input1:
  print char
  
user_input2 = input("Enter a string")
for char in user_input2:
  print char

user_input1_len = len(user_input1)
user_input2_len = len(user_input2)
if user_input1_len != user_input2_len:
  print "Not one away"
  quit()
diff = 0
i = 0
while i < user_input1_len:
  if user_input1[i] != user_input2[i]:
    diff += 1
  i += 1  
print "diff is " + str(diff)
if diff == 1:
  print "One away"
else:
  print "Not one away"

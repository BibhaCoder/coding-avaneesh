def squeeze():
  user_input = input("Enter first string: ")
  input_user = input("Enter second string: ")
  
  same_chars_in_user_inputs = set(user_input) and set(input_user)
  
  for char in same_chars_in_user_inputs:
      user_input = user_input.replace(char, "")
      input_user = input_user.replace(char, "")
  
  print(user_input)
  print(input_user)
squeeze()

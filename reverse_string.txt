
user_inputs = []

while True:
  user_input = input("Enter text (leave blank to finish): ")
  if user_input == "":
    break
  user_inputs.append(user_input)

   
print("Reversed inputs:")
for item in user_inputs:
  print(item[::-1])



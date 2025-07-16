
inputs = []

print("Enter strings")

while True:
    user_input = input("Enter input")
    if user_input == "":
        break
    inputs.append(user_input)


print("Inputs with more than 80 characters")
for item in inputs:
    if len(item) > 80:
        print(item)
        print("It had " + str(len(item)) + " characters")

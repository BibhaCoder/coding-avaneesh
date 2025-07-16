user_input = input()


digit_count = [char for char in user_input if char.isdigit()]
letter_count = [char for char in user_input if char.isalpha()]
digits_array = [0] * 10


digit_count = len(digit_count)
letter_count = len(letter_count)

print("Digits:", digit_count)
print("Letters:", letter_count)

for char in user_input:
  if char.isdigit():
    digits_array[int(char)] += 1
print digits_array

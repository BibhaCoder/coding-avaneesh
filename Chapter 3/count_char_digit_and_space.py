user_input = input()


digit_count = [char for char in user_input if char.isdigit()]
letter_count = [char for char in user_input if char.isalpha()]
digits_array = [0] * 10


digit_count = len(digit_count)
letter_count = len(letter_count)

print("Amount of Digits:", digit_count)
print("Amount of Letters:", letter_count)

white_space_count = len(user_input) - digit_count - letter_count

print("Amount of white spaces:", white_space_count)

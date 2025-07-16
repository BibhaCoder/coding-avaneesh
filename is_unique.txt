def is_unique_number():
    n = input("Enter a number: ") 
    return len(set(n)) == len(n)


if is_unique_number():
    print("Unique")
else:
    print("Not unique")

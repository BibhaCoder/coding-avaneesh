def expand():
    s1 = input("Enter start char: ")
    s2 = input("Enter end char: ")
    for char in range(ord(s1), ord(s2) + 1):
        print(chr(char))

expand()

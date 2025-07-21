def invert():
    x = int(input("Enter a number: "))
    p = int(input("Enter position: "))
    n = int(input("Amount of bits that will be inverted"))
    if n > p + 1:
        print("Invalid n:", n)
        return
    mask = ((1 << n) - 1) << (p + 1 - n)
    result = x ^ mask
    print("It changed from this " + bin(x) + " to " + bin(result))
invert()

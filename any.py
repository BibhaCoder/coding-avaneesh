def any(s1, s2):
    i = 0
    while i < len(s1):
        if s2[i] in s1:
            return ("The first time a number from s1 matches with s2 is on the " + str(i) + " character")
        i += 1
    return -1

s1 = input("Enter the first string: ")
s2 = input("Enter the second srting")

print (any(s1, s2))

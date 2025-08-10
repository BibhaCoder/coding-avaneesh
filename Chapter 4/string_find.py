def custom_find():
    s = input("Enter the main string: ")
    sub = input("Enter the substring to find: ")
    
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            print("Found at index:", i + 1)
            return i
    
    print("Not found")
    return -1

custom_find()

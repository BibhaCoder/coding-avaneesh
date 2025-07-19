def getbits():
    x = int(input("Enter number"))
    p = int(input("Enter position"))
    n = int(input("Number of bits to extract"))
    print(bin(x))
    if n > p + 1:
      print("Invalid n: " + str(n))
      return
    mask = (~(~0 << n))
    y = (x >> (p + 1 - n) & mask)
    print (bin(y))
      
        
      
      
  
getbits()

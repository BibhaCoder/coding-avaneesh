def getbits():
    x = int(input())
    p = int(input())
    n = int(input())
    print(bin(x))
    
    mask = (~(~0 << n))
    y = (x >> (p + 1 - n) & mask)
    print (bin(y))
      
        
      
      
  
getbits()

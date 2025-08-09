def itob():
  num = int(input())
  user_base = int(input())

  
  while num != 0:
    r = num % user_base
    num = num // user_base
    string_num = ""
    string_num = ("" + str(r))
    print string_num

itob()



def is_palindrome(a):
  return a == a[::-1]
  
print "Palindrome Test"

number = input("Enter a number: ")
if is_palindrome(number):
    print("It's a palindrome")
else:
    print("It's not a palindrome")

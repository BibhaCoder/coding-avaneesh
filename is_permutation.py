def is_permutation(a, b):
  return sorted(a) == sorted(b)

a = input("First string: ")
b = input("Second string: ")

if is_permutation(a, b):
    print("Permutations")
    print("(Same characters but different order)")
else:
    print("Not permutations")
    print("(Different characters")

x = "true"
y = "false"
def isVowel(letter):
  if letter in ['a', 'e', 'i', 'o', 'u']:
    return x
  else:
    return y

a = input("enter letter: ")
c = isVowel(a)
print(c)

b = input("enter letter: ")
d = isVowel(b)
print(d)
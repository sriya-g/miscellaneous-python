number = int(input("Enter a number, 0 to end: "))
while number != 0:
 o = number % 2
 if o == 0:
   print("even")
 elif o == 1:
   print("odd")
 number= int(input("Enter a number, 0 to end: "))
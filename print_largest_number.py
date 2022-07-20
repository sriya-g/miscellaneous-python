x=input("number 1 ")
y=input("number 2 ")
z=input("number 3 ")
if float(x)>float(y):
  if float(x)>float(z):
    print(x)
if float(y)>float(x):
  if float(y)>float(z):
    print(y)
if float(z)>float(x):
  if float(z)>float(y):
    print(z)
try:
  a = int(input("Enter first number:"))
  b = int(input("Enter second number:"))
  c = a/b
  print("result", c)
except ZeroDivisionError:
  print("divided by zero is not defined") 
    
else:
  print("program executed successfully")

finally:
  print("i'm always here for execute")

#

try:
  x = int(input("Enter a number:"))
except ValueError:
  print("invalid input: enter a mumber")
except ZeroDivisionError: 
  print("zero not defined")

#

try:
  with open("sampl1.txt") as f:
    content = f.read()
except FileNotFoundError:
  print("File not exist:")
else:
  print("File content:\n" + content)


 #Advanced Exception

try:
  result = float("abc")
except ValueError as x:
  print("Conversion error:", x)

#

try:
  with open("Myfile.txt", "r") as f:
    try:
      content = f.read()
      print("Data:", content)
    except IOError:
      print("Inner: File not found or inaccessible")
except FileNotFoundError:
  print("Outer: File not found")
else:
  print("File open successfully")


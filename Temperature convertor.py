print("Hello, if you want to convert from Farenheit to Celsius")
type_conversion=float(input("If you want to convert from Farenheit to Celsius type 1 or from Celsius to Farenheit type 2, do it here:  "))
number=float(input("Type here the number you want to convert right here:  "))
if type_conversion==1:
 result= number - 32
elif type_conversion==2:
 result= number + 32
else:
 result="not available because you have to type 1 or 2"
print("The result is",result)
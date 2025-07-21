age=input("Type your age as a number:  ")
try:
 if type(age)==type(""):
   print("Hey,type a number")
 else:
  if age>=18:
    print("You are an adult :)")
  elif age<0:
    print("Come on, don't lie to me")
  else:
    print("You're underage :(")
except:
   print("You didn't type the requested type of variable")
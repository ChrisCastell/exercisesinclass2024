name="Chris"
surname="Castellanos"
print(type(name),type(surname))
print(name+' '+surname)
#Size of characters
print(len(name),len(" "))
print("I'm Chris")
#Formats
info= "Hello, my name is "+ name + "and my surname is " + surname
print(info) #version1
Info= "Hello, my name is {} and my surname is {}".format(name,surname)
print(info)
text="hola_geNte"
print(len(text))
print(text,text.lower)
print(text.count("e"))
#slicing
print(text[1])
print(text[0:4])
print(text[0:5:2])
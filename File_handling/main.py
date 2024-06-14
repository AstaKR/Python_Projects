try:
    file = open("file.txt")
    dics = {"key" : "value"}
    print(dics["value"])
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("kali")
    file.write("File is created using except commands")

except KeyError:
    print(dics["key"])
    print("Oops main comments again wrong ")

else:
    content = file.read()
    print(content)
finally:
    raise NameError("This is  my revenge ")



# nubers with user input
_apple = input("Enter first number : ")

tot = int(_apple) + 50
print(tot)

tot = float(_apple) + 50
print(tot)


# Math oerations
print(3 ** 2)
print((20 - 10) * 5 + (20 - 5))

# strings
c = "Oianda Gamage"
print(c)

# # Method
# # this is to replace a letter to another. In here iam goint to replace with "i" to "s" in oianda gamage.
print(c.replace("i", "s"))

# dir use to see all the methods in python related to c variable
dir(c)
print(c.upper())

# # try this one in the command promt
help("".replace)

print("oianda Gamage".replace("i", "s"))

# let say we have a word like "here". in here we have two "e"s. if we want to replace only first "e".then,
print("here".replace("e", "i", 1))

print("hi" + "there")

# string indexing
c = "hi there"
print(c[5])
print(type(c[5]))
print(c[-3])

# to get only "hi" in the "hi there".
print(c[0:2])
print(c[0:4])
print(c[3:])
print(c[-3:-1])

print(c[5] + c[1] + c[7])

c = ["H", 2, "hi there"]
c.append(6)
c.remove(2)
print(c)

# tuples - can use any type of data types in a single variable
t = ("hello", 5, 5.7)
t[-1]

# dictionaries - can pass items
d = {"Name": "Osanda", "Last Name": "Gamage",
     "Cities": ("Matara", "Galle", "Colombo")}
print(d["Name"])
print(d["Cities"])

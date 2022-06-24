# greeting = "Good Morning, "
# name = "Harry"
# print(type(name))

# Concatenating two strings
# c = greeting + name
# print(c)
name = "Harry"
# print(name[4])
# name[3] = "d" --> Does not work

# print(name[1:4]) #includes 1,2,3, called String Slicing
# print(name[:4]) # is same as name[0:4]
# print(name[1:]) # is same as name[1:5]
# c = name[-4:-1] # is same is name[1:4]
# print(c)

name = "HarryIsGood"
# d = name[1:4:1] # 1 to 4 with skip value of 1
# d = name[0::3] # 0 till end with skip value of 3 i.e skips 3 values
d = name[:0:-1] # prints in reverse order
print(d)
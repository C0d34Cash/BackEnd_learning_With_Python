users = ["Dave", "john", "Sarah", "Mike"]
data =[1, 2, 3, "Dave", "john", "Sarah", "Mike", 4, 5, 6, True, False, 3.14, 2 + 3j]
emptylist =[]

print(3.14 in data) # returns True if the value is in the list

print(users[0]) # prints the first item in the list
print(users[-2]) # prints the last item in the list

print(users[1:3]) # prints the second and third items in the list

print(data.index(2 + 3j)) # returns the index of the specified value in the list
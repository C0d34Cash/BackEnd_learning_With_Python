users = ["Dave", "john", "Sarah", "Mike","Debojyoti"]
data =[1, 2, 3, "Dave", "john", "Sarah", "Mike", 4, 5, 6, True, False, 3.14, 2 + 3j]
emptylist =[]

print(3.14 in data) # returns True if the value is in the list

print(users[0]) # prints the first item in the list
print(users[-2]) # prints the last item in the list

print(users[1:3]) # prints the second and third items in the list

print(data.index(2 + 3j)) # returns the index of the specified value in the list

print (users[-4:-1])

print(len(data)) #Length

users.append('Sandipan') # Add new elements to the list
print(users) # Add new elements to the list

users += ['Ankan'] # Add new elements to the list
print(users)

users.extend(['Sayantan','Ayantan']) # Add new elements to the list
print(users)

#users.extend(data) #pass in pre exixting list in another list
print(users)

# Inserting new elements at a specific index
users.insert(0,"Mosha")
print(users)

users[2:2] = ["Bang", "Murgi"]
print(users)

users.remove("Dave") #Remove method
print(users)

print(users.pop()) #POP method
print(users)

print(len(users))
del users[0]

# Deleting a total list
# del users
#users.clear()



# Sorting a list
users[1:2] = ["dave"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums =[4,42,78,1,5]
nums.reverse()
print(nums)

#nums.sort(reverse=True)
#print(nums)

print(sorted(nums, reverse=True))
print(nums)

print(" ")
print(" ")

# Three different ways to copy a list
numscopy = nums.copy()
mynums = list(nums)
mycopy =nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1,"Murgi",True])
print(mylist)
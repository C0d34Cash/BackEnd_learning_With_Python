nums = {1,2,3,4}
nums1 = set(( 5,6,7,8))

print(nums)
print(nums1)
print(type(nums))
print(len(nums1))

# no duplicates allowed
one = {1,6,4,6,7,8}
print(one)

# True is a dupe for 1 and False is a dupe for 0
nums = {True,1,2,3,4,False,0,8,8,7,9}
print(nums)

# Check if a value is in a set
print(2 in nums)

#But you cannot refer to an element in the set with an index position or key


# Add a new element to a set
nums.add(10)
print(nums)

# Add elements from one set to another
morenums = {"a","b","c","d"}
nums.update(morenums)
print(nums)

# You can use updates with lists, dictionaries and tuples too


# Merge two sets to a new set
two = {99,78,67,87}
three = {90,89,45,54}

mynewset = one.union(two)
print(mynewset)

#  Keep only the duplicates
four = {1,2,3}
five = {2,3,5}

four.intersection_update(five)
print(four)

# keep everything except the duplicates
four = {1,2,3}
five = {2,3,5}
four.symmetric_difference_update(five)
print(four)
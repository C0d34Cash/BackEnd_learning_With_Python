# Tuple

mytuple = tuple(("Debojyoti","Ankan","Sandy"))

anothertuple = (1,2,3,7,7,4)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# Packing the tuple
newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

(one,two,*hey) = anothertuple # Unpacking a Tuple
print(one)
print(two)
print(hey)


# Calling a function

print(anothertuple.count(7))
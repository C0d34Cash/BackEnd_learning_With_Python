# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1


value = 1
while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("now value is equal to " + str(value))

names = ["Debojyoti","Ankan","Sandipan"]
# for x in names:
#     print(x)


# for x in ["Mississippi"]:
#     print(x)


# for x in names:
#     if x == "Sandipan":
#         break
#     print(x)



for x in names:
    if x == "Sandipan":
        continue
    print(x)
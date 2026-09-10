band = {
    "vocals": "plant",
    "Guitar": "page"
}

band2 = dict(vocals= "plant", Guitar="page")

print(band)
print(band2)

print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("Guitar"))

# List all the keys
print(band.keys())

# List all values
print(band.values())

# List all key/value pairs as tuples
print(band.items())

# Verify if a key exists
print("Guitar" in band)
print("!" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# Rwemove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) #tuple
print(band)

# Delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2
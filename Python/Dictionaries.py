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
# A dictionary is a collection of key-value pairs.
# It is unordered, changeable, and does not allow duplicate keys.

my_dict = {
    "brand": "Ford",
    "model": "Mustang Shelby GT350",
    "year": 1965
}

# Accessing values

print(my_dict["model"])  # Output: Mustang Shelby GT350

# Nested dictionaries and lists

personal_info = {
    "name": "John",
    "luckynumbers": [7, 11, 13],
    "passwords": {
        "account1": "password123"
    }
}

print(personal_info["passwords"]["account1"])  # Output: password123

print(personal_info["luckynumbers"][2])  # Output: 13


#Make changes to a list in a dictionary

d = {
    "key1": ['a', 'b', 'c'],
}

print(d)

print(d["key1"][2].upper()) # Output: C


# Appending to a dictionary

d["key2"] = [1, 2, 3] # Adding a new key-value pair

print(d)

# Updating an existing key-value pair

d["key2"] = ['one', 'two', 'three'] # Updating the value for key2

print(d)

print(d.keys())   # Output: dict_keys(['key1', 'key2'])

print(d.values()) # Output: dict_values([['a', 'b', 'c'], ['one', 'two', 'three']])

print(d.items())  # Output: dict_items([('key1', ['a', 'b', 'c']), ('key2', ['one', 'two', 'three'])])
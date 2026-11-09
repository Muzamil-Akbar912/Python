# key:value pairs in which keys are unique

info = {
    "name": "Muzamil",
    "cgpa": 8.2,
    "subject": ["Math", "CS"]
}

print(info)
print(type(info))

info["cgpa"] = 8.4
print(info["cgpa"])

# some methods in dictionary

# 1. keys() -> print all keys

dict_keys = list(info.keys())
print(dict_keys)

# 2. values() -> print all values

dict_values = list(info.values())
print(dict_values)
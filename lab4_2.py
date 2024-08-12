emp = {
    "id": 1,
    "name": "John Doe",
    "designation": "Software Engineer",
    "salary": 50000
}

print("Original dictionary:")
print(emp)

# Delete the 'designation' key
del emp["designation"]

print("\nDictionary after deleting 'designation' key:")
print(emp)

# Update the 'name'
emp["name"] = "Jane Doe"

print("\nDictionary after updating 'name':")
print(emp)
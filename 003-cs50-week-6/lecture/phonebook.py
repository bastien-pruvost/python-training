# People as list
# people = [
#     {"name": "Yuliia", "number": "+33674356488"},
#     {"name": "Marc", "number": "+33612131415"},
#     {"name": "John", "number": "+33616534292"},
# ]

# name = input("Name: ")
# for person in people:
#     if person["name"] == name:
#         print(f"✅ - Found {person["name"]} - Number: {person["number"]}")
#         break
# else:
#     print("❌ - Not found.")

# People as dictionary
people = {
    "Yuliia": "+33674356488",
    "Marc": "+33612131415",
    "John": "+33616534292",
}

name = input("Name: ")

if name in people:
    print(f"✅ - Found {name} - Number: {people[name]}")
else:
    print("❌ - Not found.")

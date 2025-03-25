import csv

name = input("Name: ")
number = input("Number: ")

# file = open("phonebook.csv", "a")

with open("phonebook.csv", "a") as file:
    # writer = csv.writer(file)
    # writer.writerow([name, number])
    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name": name, "number": number})

# We dont need to close the file when we use `with open() as `
# file.close()

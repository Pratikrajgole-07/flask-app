student = {}

student["Name"] = input("Enter Name: ")
student["PRN"] = input("Enter PRN: ")
student["Branch"] = input("Enter Branch: ")

print("Original Dictionary :", student)

student["Branch"] = input("Enter Updated Branch: ")

print("Updated Dictionary :", student)

print("\nDictionary Keys and Values:")

for key, value in student.items():
    print(key, ":", value)
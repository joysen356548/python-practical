file = open("data.txt", "w")
file.write("Python Programming\n")
file.close()

file = open("data.txt", "a")
file.write("File Handling")
file.close()

print("Data written and appended successfully")
file_name = input("Enter the file name: ")
try:
    file_handle = open(file_name)
except FileNotFoundError:
    print("The file is not found.")
    exit()

count = {}
for lines in file_handle:
    line = lines.split()
    if len(line) == 0: continue
    if not line[0] == "From": continue
    if line[2] not in count:
        count[line[2]] = 1
    elif line[2] in count:
        count[line[2]] += 1

print(count)
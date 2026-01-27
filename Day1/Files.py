name = input("Enter your file name: ")

try:
	with open(name) as fhandle:
		finding = [line for line in fhandle if line.startswith("X-DSPAM-Confidence:")]
		if len(finding) == 0:
			print("There is no spam confidence")
			exit()
except FileNotFoundError:
	print("The file is not found")
	exit()

numbers = []

for data in finding:
	try:
		number = data[data.find(":")+1:].strip()
		number = float(number)
		numbers.append(number)
	except ValueError:
		print(f"There is no value or there is a wrong value: {number}")
		exit()

average = sum(numbers)/len(numbers)

print(f"Average spam confidence: {average}")
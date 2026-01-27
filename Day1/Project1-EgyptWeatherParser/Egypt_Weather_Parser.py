import csv

temperatures = []
with open("Cairo-Weather.csv", newline="") as file:
	entries = csv.reader(file)
	next(entries)

	for entry in entries:
		date_temperature = {}
		if entry[0] == "" or entry[3] == "": continue
		try:
	    		date_temperature["date"] = entry[0]
	    		date_temperature["temperature"] = float(entry[3])
		except ValueError:
	    		print("There is a wrong number")
	    		exit()
		temperatures.append(date_temperature)

filtered_temperature = [day for day in temperatures if day["temperature"] > 30]

def get_temperature(day):
    return day["temperature"]
filtered_temperature.sort(key=get_temperature,reverse =True)

for i , day in enumerate(filtered_temperature[:5],start =1):
	print(f"{i}. Hottest day: {day['date']} - {day['temperature']}")
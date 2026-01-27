import csv

temperatures = []
Hot,Warm,Cool,Extremes = 0,0,0,0

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

for day in temperatures:
    temp = day["temperature"]
    month = int(day["date"].split()[0].split("-")[1])
    if temp > 30:
        Hot += 1
        if month >= 6 and month <= 9:
            Extremes += 1
    elif temp > 20:
        Warm += 1
    else:
        Cool += 1

def get_temperature(day):
    return day["temperature"]
filtered_temperature.sort(key=get_temperature,reverse =True)

for i , day in enumerate(filtered_temperature[:5],start =1):
	print(f"{i}. Hottest day: {day['date']} - {day['temperature']}")

print(f"Hot days: {Hot}")
print(f"Extreme days: {Extremes}")
print(f"Warm days: {Warm}")
print(f"Cool days: {Cool}")
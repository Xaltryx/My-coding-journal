import csv

#Create a new list
temperatures = []
Hot,Warm,Cool,Extremes,Humid_Hot = 0,0,0,0,0

import csv

temperatures = []

# Open the file
with open("Cairo-Weather.csv", newline="") as file:
    entries = csv.reader(file)
    next(entries)  # skip header

    # Loop through file lines
    for entry in entries:
        date_temperature = {}

        if entry[0] == "" or entry[3] == "" or entry[22] == "":
            continue

        try:
            date_temperature["date"] = entry[0]
            date_temperature["temperature"] = float(entry[3])
            date_temperature["humidity"] = float(entry[22])
        except ValueError:
            print("There is a wrong number")
            exit()

        temperatures.append(date_temperature)

#filter the temperature which is more than 30
filtered_temperature = [day for day in temperatures if day["temperature"] > 30]

#Checks the temperature and describe the day
for day in temperatures:
    temp = day["temperature"]
    month = int(day["date"].split()[0].split("-")[1])
    humid = day["humidity"]
    if temp > 30:
        Hot += 1
        if month >= 6 and month <= 9:Extremes += 1
    elif temp > 20:Warm += 1
    else: Cool += 1
    if temp > 30 and humid >50: Humid_Hot +=1

#Get the temperature from the dictionary
def get_temperature(day):
    return day["temperature"]
filtered_temperature.sort(key=get_temperature,reverse =True) #Sort the temperature descendingly

for i , day in enumerate(filtered_temperature[:5],start =1):
	print(f"{i}. Hottest day: {day['date']} - {day['temperature']}") #Print the top 5 hottest dates

#Print the summary of the days
print("\nSummary of the days:")
print(f"Hot days: {Hot}")
print(f"Extreme days: {Extremes}")
print(f"Humid Hot days: {Humid_Hot}")
print(f"Warm days: {Warm}")
print(f"Cool days: {Cool}")
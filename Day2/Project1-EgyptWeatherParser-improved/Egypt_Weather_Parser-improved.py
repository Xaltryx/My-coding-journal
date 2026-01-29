import csv
from datetime import datetime

#Create a new list
temperatures = []
Days_Summary = {"Hot":0,"Extreme":0,"Warm":0,"Cool":0,"Humid Hot":0}
HOT_TEMP,WARM_TEMP,HUMIDITY_THRESHOLD = 30,20,50

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
            date_temperature["date"] = entry[0].strip()
            date_temperature["temperature"] = float(entry[3].strip())
            date_temperature["humidity"] = float(entry[22].strip())
        except ValueError:
            print("There is a wrong number")
            continue

        temperatures.append(date_temperature)

#filter the temperature which is more than 30
filtered_temperature = [day for day in temperatures if day["temperature"] > 30]

#Checks the temperature and describe the day
for day in temperatures:
    temp = day["temperature"]
    date = datetime.strptime(day["date"].split()[0],"%Y-%m-%d")
    month = date.month
    humid = day["humidity"]
    if temp > HOT_TEMP:
        Days_Summary["Hot"] += 1
        if month >= 6 and month <= 9:Days_Summary["Extreme"] += 1
        if humid > HUMIDITY_THRESHOLD: Days_Summary["Humid Hot"] +=1
    elif temp > WARM_TEMP:Days_Summary["Warm"] += 1
    else: Days_Summary["Cool"] += 1

def classify(user_day):
    try: dth = [day for day in temperatures if day["date"].split()[0] == user_day.strip()][0]
    except IndexError:
        print("You have written something wrong")
        return "Data not found"
    date = datetime.strptime(dth["date"].split()[0], "%Y-%m-%d")
    month = date.month
    humid = dth["humidity"]
    temp = dth["temperature"]
    if temp > HOT_TEMP:
        if month >= 6 and month <= 9 and humid > HUMIDITY_THRESHOLD: return "Extreme Humid Hot"
        elif month >= 6 and month <= 9: return "Extreme"
        elif humid > HUMIDITY_THRESHOLD: return "Humid Hot"
        else: return "Hot"
    elif temp > WARM_TEMP:return "Warm"
    else:return "Cool"
#Get the temperature from the dictionary
def get_temperature(day):
    return day["temperature"]
filtered_temperature.sort(key=get_temperature,reverse =True) #Sort the temperature descendingly

for i , day in enumerate(filtered_temperature[:5],start =1):
	print(f"{i}. Hottest day: {day['date']} - {day['temperature']}") #Print the top 5 hottest dates

#Make function the summary of the days
def summary():
    print("\nSummary of the days:")
    for description in Days_Summary.items():
        print(f"{description[0]} days: {description[1]}")

summary()
print(f"\nThe type of day (2011-05-28): {classify('2011-05-28')}")
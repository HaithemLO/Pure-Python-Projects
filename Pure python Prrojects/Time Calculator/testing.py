import re

start = "3:00 PM"
Duration = "3:10"

#how many days has passed
days = 0

#Splits the Duration Time into time and am/pm
startTimeSplit = start.split()

#assigns time and am/pm to variales
startTime = startTimeSplit[0]
ampm = startTimeSplit[1]

#splits the start time in minutes/hours
time = startTime.split(":")
hours = int(time[0])
minutes = int(time[1])


#Finds the total amount of minutes duration
DurationTime = Duration.split(":")
totalMinutes = (int(DurationTime[0])*60) + int(DurationTime[1])

while totalMinutes > 60 :
    
    temp = 60-minutes
    minutes += temp
    totalMinutes = totalMinutes -temp
    
    if minutes == 60 :
        hours += 1
        minutes = 0
        if hours == 12 :
            hours = 0
            if ampm == "AM" :
                ampm ="PM"

            if ampm == "PM" :
                ampm = "AM"
                days +=1

remainingminutes = totalMinutes + minutes

if remainingminutes >= 60:
    hours += 1
    minutes = remainingminutes - 60
    if hours == 12 :
        hours = 0
        if ampm == "AM" :
            ampm ="PM"

        if ampm == "PM" :
            ampm = "AM"
            days +=1
else :
    minutes = totalMinutes




finalHours = str(hours)
finalMinutes = str(minutes)
finalDays = str(days)


if finalDays == "0" :
    finalTime = finalHours + ":" + finalMinutes +" "+ ampm
elif finalDays == "1" :
    finalDays = "the next day"
    finalTime = finalHours + ":" + finalMinutes +" "+ ampm +" "+ finalDays
else :
    finalTime = finalHours + ":" + finalMinutes +" "+ ampm +" "+finalDays + ' Days has passed sinced your start date'


# print(finalDays)
# print(finalTime)
# print(hours)  
# print(minutes) 
# print(ampm)

week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

x = "3"
print("0"+x)



            


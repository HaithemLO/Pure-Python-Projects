def add_time(start, duration,day=None):

    week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    
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
    DurationTime = duration.split(":")
    totalMinutes = (int(DurationTime[0])*60) + int(DurationTime[1])

    #Calculates how much time has passed
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

                else :
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

            else :
                ampm = "AM"
                days +=1
    else :
        minutes = totalMinutes

    # determines the day of the week
    if day != None :
        newDay = day.lower()
        newDay = newDay.capitalize()
        weekday = days
        day_place = week.index(newDay)
        
        while weekday > 0 :
            new_day_position = day_place + weekday
            if new_day_position > 6 :
                weekday = weekday -(6-day_place)
                day_place = 0
                new_day_position = 0

            else :
                finalWeekDay = week[new_day_position]
                weekday = 0
                
    #Sorts out the formatting of the output
    finalHours = str(hours)
    finalMinutes = str(minutes)
    finalDays = str(days)

    if int(finalHours) < 10 :
        finalHours = "0"+finalHours
    if int(finalMinutes) < 10 :
        finalMinutes = "0" +finalMinutes

    if day == None :
        finalWeekDay = ''

    if finalDays == "0" :
        finalTime = finalHours + ":" + finalMinutes +" "+ ampm
    elif finalDays == "1" :
        finalDays = "the next day"
        finalTime = finalHours + ":" + finalMinutes +" "+ ampm +" "+finalDays + finalWeekDay
    else :
        finalTime = finalHours + ":" + finalMinutes +" "+ ampm+", "+ finalWeekDay +" "+finalDays + ' Days Later'

    print(finalTime)
    
    
add_time("11:43 PM", "24:17", "tueSday")
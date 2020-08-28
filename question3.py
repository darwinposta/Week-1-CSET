kmRan = 14 
milesRan = kmRan * 1.609 #distance ran in miles

timeMinutes = 45.5
timeHours = timeMinutes / 60 #converts minutes ran into hours, to prepare for miles per hour

roughMPH = milesRan / timeHours #calculates MPH

overallMPH = round(roughMPH, 2) #rounds MPH to the nearest hundredth so you dont get a long float, makes it look nicer

print("the average running speed was", overallMPH,"miles per hour") #end print statement
#######################################################
#
# COSC 140 Homework 2, "bus trip planner" problem
#
#######################################################

current= int(input ("What is the departure time(in HHMM)?"))
dist= int(input("How far (in km) is the bus ride? "))
stops= int(input("How many stops is the bus making?"))

currenth,currentm = divmod(current,100)
#print(currenth) #currentm is just the number in the HOUR of the departure time 
#print(currentm) #currentm is just the number in the MINUTES of the departure time 

travh,travleftm= divmod(dist,40)
travm= int(travleftm/40*60) 
if travleftm % 2 == 0: #this is saying if the remainder is even then simple use the remainder to find the minutes needed and then set travel seconds to 0
  travs=0
else: #this is saying is the remainder is odd, then there will need to be an additional seconds to take into account, which we will assume is 30 seconds given that all distances are given in integers
  travs=30

#print(travh) #travh is the HOURS need to travel the distance at a rate of 40km/hr
#print (travleftm) #travleftm is the remainder, need to divide by 40km/hr to get fraction of hour, then multiply by 60min/hour to get minutes
#print(travm) #travm is the MINUTES need to travel the distance at a rate of 40km/hr
#print(travs) #travs is the SECONDS needed to travel the distance at a rate of 40 km/hr


stoptime=stops*30 #stoptime is how many seconds taken if each stop is 30 seconds
stopmin,stopsec=divmod(stoptime,60)
#print(stopmin) 
#print(stopsec)

tempsec=stopsec+travs
additionalmin,totalsec=divmod(tempsec,60)
#print(additionalmins) #here additional minutes included in case the seconds for stopping and traveling exceed 60
tempmins=int(currentm+travm+stopmin+additionalmin)
#print(mins) #here tempmins is the temporary minute variable, or the total minutes needed to travel and to stop added to the current time
additionalhour,totalmin=divmod(tempmins,60)
#print(additionalhour)#additionalhour is included here in case the number of minutes exceed 60, in which case the additional hour(s) will just be added on to the total hour
#print(totalmin)
totalhour=currenth+travh+additionalhour
if totalhour>=24:
  totalhour= totalhour-24




print("Your arrival time will be " + f"{totalhour:02d}"+ ":" + f"{totalmin:02d}"+ ":"+ f"{totalsec:02d}")

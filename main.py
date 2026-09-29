import requests
import time 
from bs4 import BeautifulSoup

weekend = [4,5,6]   # 4 = Friday, 5 = Saturday, and Sunday = 6
weekday = [0,1,2,3] # 0 = Monday, Tuesday = 1, Wednesday = 3, and Thursday = 3
curr_day = time.localtime() # Create's a tuple which will be used for info related to the time.
now = curr_day.tm_hour * 60 + curr_day.tm_min # converts the hours to minutes to make math easier.

def main(): # This will be the main function of the program which makes it easier to keep track of what function is doing what
    place = loc()
    if place == "butterfield":
        result = butterfield()
    elif place == "mainfare":
        result == "mainfare"
    print(f"now")

def nutironal_info_fetcher(result):
    None

def loc():

    location = input("Where would you like to eat? ") # Seeing where on campus they would want to eat.

    if location.lower().strip() == "butterfield": 
        return "butterfield"
    
    if location.lower().strip() == "mainfare": 
        return "mainfare"
    
def butterfield():
    #Butterfield is closed on the weekend
    if curr_day.tm_wday == 5 or curr_day.tm_wday == 6:
        print("Butterfield is closed on Saturday/Sunday, sorry :(")
        return ["butterfield", "closed"]  
    
    #What times Butterfield is open throughout the week 
    elif curr_day.tm_mday in weekday:
        if 7*60 <= now < 11*60 + 30:        # 7:00 AM – 11:30 AM
            return ["butterfield", "breakfast"]
        elif 12*60 <= now < 15*60 + 30:          # 12:00 PM – 3:30 PM
            return ["butterfield", "lunch"]
        elif 16*60 + 30 <= now < 20*60 + 30: #4:30PM - 8:30PM
            return ["butterfield", "dinner"]
        else:
            print("Butterfield is closed right now.")
            return ["butterfield", "closed"]
        
    # What times Butterfield is open on Friday
    else:
        if 7*60 <= now < 11*60 + 30:        # 7:00 AM – 11:30 AM
            return ["butterfield", "breakfast"]
        elif 12*60 <= now < 14*60:          # 12:00 PM – 2:00 PM
            return ["butterfield", "lunch"]
        else:
            print("Butterfield is closed right now.", now)
            return ["butterfield", "closed"]

def mainfare():
    #Mainfare during the week
    if curr_day.tm_wday in weekday:
        if 11*60 + 30 <= now < 15*60:       # 11:30 AM - 3:00 PM
            return ["mainfare", "lunch"]
        if (16*60 <= now < 21*60)           # 4:00 PM -  9:00 PM
            return ["mainfare", "dinner"]
    #Mainfare hours on Friday
    elif curr_day.tm_wday == 4:
        if 11*60 + 30 <= now < 15*60:       # 11:30 AM - 3:00 PM
            return ["mainfare", "lunch"]
        elif (16*60 <= now < 20*60)           # 4:00 PM -  8:00 PM
            return ["mainfare", "dinner"]
        else:
            print("Mainfare is closed right now")
            return ["mainfare", "closed"]
    #Mainfare hours on Saturday    
    elif curr_day.tm_wday == 5:
        if 9*60 <= now < 10*60:
            return ["mainfare", "continental breakfast"]
        elif 10*60 <= now < 15*60:
            return ["mainfare","breakfast"]
        elif 16*60 <= now < 20*60:
            return ["mainfare", "dinner"]
        else:
            print("Mainfare is closed right now")
    #Mainfare hours on Sunday
    else:
        if 9*60 <= now < 10*60:
            return ["mainfare", "continental breakfast"]
        elif 10*60 <= now < 15*60:
            return ["mainfare","breakfast"]
        elif 16*60 <= now < 21*60:
            return ["mainfare", "dinner"]
        else:
            print("Mainfare is closed right now")

main()













''' 
Reason's for why

    I used the time module so that the program would be able to give food reccomendations based upon the time of day, and day of the week sinces those are factors in what is avaiable on campus.
'''
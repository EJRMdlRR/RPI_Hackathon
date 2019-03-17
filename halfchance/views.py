from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
import json
import urllib.request
from urllib.request import urlopen
import random
from datetime import datetime
import calendar

# class Restaurant:
#   def __init__(self, name, address):
#     self.name = name
#     self.address = address


def getResturantByPrice(locationCode, budget):
    #Gets list of resturant data
    resturants = json.load(urlopen("http://api.tripadvisor.com/api/partner/2.0/location/" \
                             + locationCode \
                             +"/restaurants?key=1a389592-f59a-42dc-ba30-9695ed10b358"))
    ratingThreshold = 3.0
    ratingInterval = 0.1    
    resturantThreshold = 10
    restRatioThreshold = 3
    tries = 0
    triesThreshold = 10
    count = 0    
    badResturants = []
    goodResturants = []
    #Fills good and bad list with possible resturants in price level and rating
    found = False
    while (not found):
        badResturants.clear()
        goodResturants.clear()        
        #sort resturants into good & bad based on rating
        for resturant in resturants["data"]:
            if float(resturant["rating"]) < ratingThreshold and resturant["price_level"].count("$") <= budget.count("$"):
                badResturants.append(resturant)
            elif resturant["price_level"].count("$") <= budget.count("$"):
                goodResturants.append(resturant)
        #changes rating if one list is too heavy
        if not (len(badResturants)/len(goodResturants) < restRatioThreshold < restRatioThreshold + 0.5):
            tries += 1
            if tries == triesThreshold:
                found = True
            restRatioThreshold += ratingInterval
        else:
            tries += 1
            if tries == triesThreshold:
                found = True
            restRatioThreshold -= ratingInterval
    return goodResturants

def getResturantDishes(resturants, genre, allFoodDishes):
    goodResturants = []
    for resturant in resturants:
        #???will contain all cuisines
        if resturant["description"]:
            L = resturant["description"].lower().split()
        else:
            L = []   
        for word in L:
            if word in allFoodDishes:
                goodResturant.append(resturant)
        L.clear() 
    return goodResturants

def getResturantsNever(locationCode, budget, genre, allFoodDishes):
    goodResturantsCopy = getResturantByPrice(locationCode, budget)
    goodResturants = []
    count = 0
    #Loops through resturants and finds those with food type options in genre
    for resturant in goodResturantsCopy:
        resturantFoodTypes = [ x["name"] for x in resturant["cuisine"] ]  

        for foodType in genre:
            if foodType in resturantFoodTypes:
                count += 1 #######
        if count > 0:
            goodResturants.append(resturant)
        count = 0
    goodResturants.extend(getResturantDishes(goodResturantsCopy \
                                             , genre, allFoodDishes))
    return list(goodResturants)

def is_open(objects):
    boolean = False
    address = objects.get('address_obj')
    hours = objects.get('hours')
    if hours != None:
        week_ranges = hours.get('week_ranges')
        for day_info in week_ranges:
            day = day_info.get('localized_day_name')
            if day == calendar.day_name[datetime.today().weekday()]:
                print(day)
                times = day_info.get('times')
                if times != []:
                    open_t = (times[0].get('open_time')).split(':')
                    close_t = (times[0].get('close_time')).split(':')
                    time_open = float(open_t[0]) + (float(open_t[1]) / 60)
                    time_closed = float(close_t[0]) + (float(close_t[1]) / 60) - 1
                    current = datetime.now()
                    present = float(current.hour) + float(current.minute / 60)
                    if time_closed < 5:
                        if time_open < present:
                            boolean = True
                    elif time_open < present < time_closed:
                        boolean = True
                else:
                    boolean = False
    else:
        boolean = True
    print(boolean)
    return boolean 


# Create your views here.
def index(request):
    return render(request, 'index.html')

def fiftyfifty(request):
    data = json.load(urllib.request.urlopen("http://api.tripadvisor.com/api/partner/2.0/location/48739/restaurants?key=1a389592-f59a-42dc-ba30-9695ed10b358"))
    info = data.get('data')
    options = []

    for objects in info:
        # print(objects)
        if is_open(objects):
            ratings = float(objects.get('rating'))
            if (ratings >= 4) or (ratings <= 2):
                address = objects.get('address_obj')
                options.append(address.get('address_string'))

    print(options)
    if options != []:
        output = options[random.randrange(0, len(options))]
    else:
        output = "No available restaurants"
    return render(request, 'address.html', context={'output':output})

def never(request):
    # restaurants = getResturantsNever('48739', '$$', ['american', 'asian'], [])
    # print('RESTAURANTS')
    # print(restaurants)
    # restuarants = ['']
    locationCode = [420263, 7376336, 7193910, 10490853, 1153096, 2093018]
    r = []
    for x in locationCode:
        r.append(json.load(urlopen("http://api.tripadvisor.com/api/partner/2.0/location/" \
                             + str(x) \
                             +"/restaurants?key=1a389592-f59a-42dc-ba30-9695ed10b358"))["data"][0])
    restaurant = random.choice(r)
    print(restaurant)
    return render(request, 'never.html', context={'restaurant':restaurant})
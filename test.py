"""
Title: Never Have I Ever
The purpose of this code is to us the TripAdvisor API to analyze restaurants
nearby and give food recommendations based on foods/things that are new to the
user(s).

Author: Quinn Bardwell
Date: 03/16/19
"""
import random
import json
from urllib.request import urlopen

def getZipcode(zipcode):  #doesnt work
    pass

def getLongLat(address):  #doesnt work      
    address="1600+Amphitheatre+Parkway,+Mountain+View,+CA"
    key="my-key-here"
    url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address, key)
    
    response = urllib2.urlopen(url)
    jsongeocode = response.read()

def getResturants5050(locationCode, budget):
    #List of resturant data
    resturants = json.load(urlopen("http://api.tripadvisor.com/api/partner/2.0/location/" \
                             + userLocation \
                             +"?key=2f5aef9e-d399-4298-9986-ea6305c270a8"))
    ratingThreshold = 3.0
    tries = 0
    triesThreshold = 10
    ratingInterval = 0.1
    badResturants = []
    goodResturants = []
    #fills good and bad list with possible resturants in price level and rating
    found = False
    while (not found):
        badResturants.clear()
        goodResturants.clear()        
        #sort resturants into good & bad based on rating
        for resturant in resturants:
            if resturant["rating"] < ratingThreshold and resturant["price_level"].count("$") <= budget.count("$"):
                badResturants.append(resturant)
            elif resturant["price_level"].count("$") <= budget.count("$"):
                goodResturants.append(resturant)
        #changes rating if one list is too heavy
        if not (0.75 < len(badResturants)/len(goodResturants) < 1.33):
            tries += 1
            if tries == triesThreshold:
                found = True
            if len(badResturants) > len (goodResturants):
                ratingThreshold -= ratingInterval
            else:
                ratingThreshold += ratingInterval
        else:
            found = True
    return (random.choice(badResturant), random.choice(goodResturant))

#budget is a string like this => "$$" & genre is a list of food type that they
#have not tried
def getResturantsNever(locationCode, budget, genre, allFoodTypes):
    #List of resturant data
    resturants = json.load(urlopen("http://api.tripadvisor.com/api/partner/2.0/location/" \
                             + userLocation \
                             +"?key=2f5aef9e-d399-4298-9986-ea6305c270a8"))
    ratingThreshold = 3.0
    ratingInterval = 0.1    
    resturantThreshold = 10
    restRatioThreshold = 3
    tries = 0
    triesThreshold = 10
    count = 0    
    badResturants = []
    goodResturants = []
    #fills good and bad list with possible resturants in price level and rating
    found = False
    while (not found):
        badResturants.clear()
        goodResturants.clear()        
        #sort resturants into good & bad based on rating
        for resturant in resturants:
            if resturant["rating"] < ratingThreshold and resturant["price_level"].count("$") <= budget.count("$"):
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
            restRatioThreshold -= ratingInterval
        else:
            found = True
    goodResturantsCopy = goodResturants.copy()
    goodResturants.clear()
    
    for foodType in allFoodTypes:
        pass
    #loops thru dish options
    for resturant in goodResturantsCopy:
        resturantFoodTypes = [ x["name"] for x in resturant["cuisine"] ]  
        resturantDishes = []
        L = [] #will contain all dishes 
        if resturant["description"]:
            L = resturant["description"].lower().split()
        for words in [x["text"].lower().split() for x in resturant["reviews"] ]:
            L.extent(words)
        for foodType in allFoodTypes:
            for food in foodType:
                if food in L:
                    count += 1 #######
        for foodType in genre:
            for resturantFoodType in resturantFoodTypes:
                if foodType == resturantFoodType:
                    count += 1 #######
            for resturantDish in resturantDishes:
                if resturantDish in allFoodTypes:
                    count += 1 #######
        if count > 0:
            goodResturants.append(resturant)
    return random.choice(goodResturants)

if __name__ == "__main__":

    #userZipcode = input("What is your zipcode? ")
    userLongLat = ""#getLongLat(userZipcode)
    
    userLocation = "2093018"#getZipcode(userZipcode)
    
    data = json.load(urlopen("http://api.tripadvisor.com/api/partner/2.0/location/" \
                             + userLocation \
                             +"?key=2f5aef9e-d399-4298-9986-ea6305c270a8"))
    
    keys2 = data["address_obj"].keys()
    
    allFoodTypes = ["american", "asian", "bar", "barbecue", "brew pub", "cafe" \
            , "caribbean", "central european", "chinese", "contemporary" \
            , "cuban", "deli", "diner", "eastern european","european" \
            , "fast food", "gastropub", "greek", "grill", "hawaiian", "healthy" \
            ,"hong kong", "indian", "indonesian", "international", "irish" \
            , "italian", "japanese", "korean", "latin", "lebanese" \
            , "mediterranean", "mexican", "middle eastern", "moroccan" \
            , "pakistani", "pizza", "polish", "pub", "seafood", "shanghai" \
            , "soups", "spanish" , "steakhouse", "street food", "sushi" \
            , "szechuan", "taiwanese", "thai", "turkish", "wine bar"]

    print (data)
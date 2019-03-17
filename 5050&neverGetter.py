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

def getZipcode(zipcode):  #to do
    pass

def getLongLat(address):  #to do     
    address="1600+Amphitheatre+Parkway,+Mountain+View,+CA"
    key="my-key-here"
    url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address, key)
    
    response = urllib2.urlopen(url)
    jsongeocode = response.read()

#Testish function for 5050
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


"""
This function takes the geo-code and the budget (as "$" to "$$$$") and sorts
through all of the resturants to find the top ~25% (by rating) that are in the
user's price range. Then, we return a list of these resturant objects.
"""
def getResturantByPrice(locationCode, budget):
    #Gets list of resturant data
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
    #Fills good and bad list with possible resturants in price level and rating
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
            tries += 1
            if tries == triesThreshold:
                found = True
            restRatioThreshold -= ratingInterval
    return goodResturants

"""
This function takes genre (cuisines & dishes wanted) and a list of resturants
and a list of all possible food dishes then, adds the resturants that have
wanted dishes to a list and returns it.
"""
def getResturantDishes(resturants, genre, allFoodDishes):
    goodResturants = []
    for resturant in resturants:
        #???will contain all cuisines
        if resturant["description"]:
            L = resturant["description"].lower().split()
        else:
            L = []
        for words in [x["text"].lower().split() for x in resturant["reviews"] ]:
            L.extend(words)        
        for word in L:
            if word in allFoodDishes:
                goodResturant.append(resturant)
        L.clear() 
    return goodResturants

"""
This function take in geoCode and budget, gets a list of possible resturants
from that and then finds the resturants which fall into the genre (food types
and dishes) category. Returns list of suitable resturants.
"""
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
    return goodResturants

if __name__ == "__main__":

    userLocation = "2093018"#getZipcode(userZipcode)
    data = json.load(urlopen("http://api.tripadvisor.com/api/partner/2.0/location/" \
                             + userLocation \
                             +"?key=2f5aef9e-d399-4298-9986-ea6305c270a8"))
        
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
    
    allFoodDishes = ['bagels', 'baguette', 'bananas foster', 'bibimbap' \
                     , 'calamari', 'cheeseburger', 'cheesecake', 'cheesesteak' \
                     , 'chicken and waffles', 'chicken wings', 'chili' \
                     , 'chowder', 'clam chowder', 'corned beef', 'crab', 'crab' \
                     , 'cake cupcake', 'cupcakes', 'dim sum', 'dumplings' \
                     , 'eggs benedict', 'falafel', 'filet mignon' \
                     , 'fish & chips', 'fish taco', 'french toast' \
                     , 'fried pickles', 'grilled cheese', 'gyros', 'hamburger' \
                     , 'hot dog', 'ice cream', 'jambalaya', 'juice & smoothies' \
                     , 'lasagne', 'lobster', 'lobster roll', 'mac and cheese' \
                     , 'mandarin duck', 'meatloaf', 'moussaka', 'nachos' \
                     , 'noodle', 'omelette', 'oyster', 'pad thai', 'pancakes' \
                     , 'pasta', 'peking duck', 'poutine', 'pretzel', 'ramen' \
                     , 'ribs', 'roast beef', 'salad', 'saltimbocca' \
                     , 'sandwiches', 'schnitzel', 'shawarma', 'shrimp' \
                     , 'surf and turf', 'tacos', 'tapas', 'tempura' \
                     , 'tortillas', 'waffles', 'waffles & crepes', 'wings']

    print([x.strip() for x in allFoodDishes.lower().split(",")])
    
    print (data)
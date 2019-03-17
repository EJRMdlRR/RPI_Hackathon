import json
import urllib.request
import random
from datetime import datetime
import calendar

def is_open(objects):
    address = objects.get('address_obj')
    ratings = objects.get('rating')
    hours = objects.get('hours')
    if hours != None:
        week_ranges = hours.get('week_ranges')
        for day_info in week_ranges:
            day = day_info.get('localized_day_name')
        if day == calendar.day_name[datetime.today().weekday()]:
            return True
        else:
            return False
    else:
        return True

data = json.load(urllib.request.urlopen("http://api.tripadvisor.com/api/partner/2.0/location/48739/restaurants?key=2f5aef9e-d399-4298-9986-ea6305c270a8"))
info = data.get('data')
options = []

for objects in info:
    if is_open(objects):
        ratings = float(objects.get('rating'))
        if (ratings > 4) or (ratings < 2):
            address = objects.get('address_obj')
            options.append(address.get('address_string'))

print(options[random.randrange(0,len(options))])
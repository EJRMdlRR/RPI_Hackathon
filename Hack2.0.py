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
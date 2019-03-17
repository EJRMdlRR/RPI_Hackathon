'''
import json
import urllib.request
import random
from datetime import datetime
import calendar

data = json.load(urllib.request.urlopen("http://api.tripadvisor.com/api/partner/2.0/location/48739/restaurants?key=2f5aef9e-d399-4298-9986-ea6305c270a8"))
info = data.get('data')
options = []


def is_open(objects):
    address = objects.get('address_obj')
    ratings = objects.get('rating')
    hours = objects.get('hours')
    if hours != None:
        week_ranges = hours.get('week_ranges')
        for day_info in week_ranges:
            times = day_info.get('times')
            if times != []:
                print(times)
                open_t = (times[0].get('open_time')).split(':')
                close_t = (times[0].get('close_time')).split(':')
                time_open = float(open_t[0]) + (float(open_t[1]) / 60)
                time_closed = float(close_t[0]) + (float(close_t[1]) / 60) - 1
                current = datetime.now()
                present = float(current.hour) + float(current.minute / 60)
                if time_closed < 5:
                    if time_open < present:
                        return True
                elif time_open < present < time_closed:
                    return True
            else:
                return False
        else:
            return True
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
    return boolean    

for objects in info:
    print(is_open(objects))
'''

cities = [('Hong Kong, China','294217'), ('Singapore','294265'), ('Bangkok, Thailand','293916'), \
('London,United Kingdom','186338'), ('Paris, France','187147'), ('Macau','664891'), ('New York City, USA','60763'), \
('Shenzhen, China','297415'), ('Kuala Lumpur, Malaysia','298570'), ('Antalya, Turkey','297962'), \
('Istanbul, Turkey','293974'), ('Dubai, United Arab Emirates','295424'), ('Seoul, South Korea','294197'), \
('Rome, Italy','187791'), ('Phuket, Thailand','293920'), ('Guangzhou, China','298555'), ('Mecca, Saudi Arabia','293993'), \
('Pattaya, Thailand','293919'), ('Taipei, Taiwan','293913'), ('Miami, USA','34439'), ('Prague, Czech Republic','274707'), \
('Shanghai, China','308272'), ('Las Vegas, USA','45963'), ('Milan, Italy','187849'), ('Barcelona, Spain','187497'), \
('Moscow, Russia','294459'), ('Amsterdam, Netherlands','188590'), ('Vienna, Austria','190454'), ('Venice, Italy','187870'), \
('Los Angeles, USA','32655'), ('Lima, Peru','32655'), ('Tokyo, Japan','298184'), ('Johannesburg, South Africa','312578'), \
('Beijing, China','294212'), ('Sofia, Bulgaria','294452'), ('Orlando, USA','34515'), ('Berlin, Germany','187323'), \
('Budapest, Hungary','274887'), ('Ho Chi Minh City, Vietnam','293925'), ('Florence, Italy','187895'), \
('Madrid, Spain','187514'), ('Warsaw, Poland','274856'), ('Doha, Qatar','294008'), ('Nairobi, Kenya','294207'), \
('Delhi, India','304551'), ('Mumbai, India','304554'), ('Chennai, India','304556'), ('Mexico City, Mexico','150800'), \
('Dublin, Ireland','186605'), ('San Francisco, USA','60713'), ('Hangzhou, China','298559'), ('Denpasar, Indonesia','297694'), \
('St. Petersburg, Russia','298507'), ('Mugla, Turkey','1221512'), ('Brussels, Belgium','188644'), ('Burgas, Bulgaria','635766'), \
('Munich, Germany','187309'), ('Zhuhai, China','297418'), ('Sydney, Australia','255060'), ('Edirne, Turkey','652369'), ('Toronto, Canada','155019'), \
('Lisbon, Portugal','189158'), ('Cancún, Mexico','150807'), ('Buenos Aires, Argentina','312741'), ('Cairo, Egypt','294201'), \
('Punta Cana, Domincan Republic','147293'), ('Suzhou, China','297442'), ('Djerba, Tunisia','297941'), ('Agra, India','297683'), \
('Kraków, Poland','274772'), ('Bucharest, Romania','294458'), ('Siem Reap, Cambodia','297390'), ('Jaipur, India','304555'), \
('Honolulu, USA','60982'), ('Manama, Bahrain','293997'), ('Dammam, Saudi Arabia','298547'), ('Hanoi, Vietnam','293924'), \
('Andorra La Vella, Andorra','190392'), ('Nice, France','187234'), ('Zürich, Switzerland','188113'), \
('Jakarta, Indonesia','294229'), ('Manila, Philippines','298573'), ('Chiang Mai, Thailand','293917'), \
('Marrakech, Morocco','293734'), ('Sharm El Sheikh, Egypt','297555'), ('Marne-La-Vallée, France','226865'), \
('Frankfurt, Germany','187337'), ('Abu Dhabi, United Arab Emirates','294013'), ('Vancouver, Canada','154943'), \
('Guilin, China','298556'), ('Melbourne, Australia','255100'), ('Rio De Janeiro, Brazil','303506'), \
('Riyadh, Saudi Arabia','293995'), ('Amman, Jordan','293986'), ('Sousse, Tunisia','295401'), ('Kiev, Ukraine','294474'), \
('Sharjah, United Arab Emirates','298064'), ('Jeju Island, South Korea','983296'), ('Krabi, Thailand','297927'), \
('Artvin, Turkey','652371')]










for city in cities:
    print(city)
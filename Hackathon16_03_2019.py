from datetime import datetime
import math
cities = [('Hong Kong, China','Home-g294217'), ('Singapore','Home-g294265'), ('Bangkok, Thailand','Home-g293916'), \
('London,United Kingdom','Home-g186338'), ('Paris, France','Home-g187147'), ('Macau','Home-g664891'), ('New York City, USA','Home-g60763'), \
('Shenzhen, China','Home-g297415'), ('Kuala Lumpur, Malaysia','Home-g298570'), ('Antalya, Turkey','Home-g297962'), \
('Istanbul, Turkey','Home-g293974'), ('Dubai, United Arab Emirates','Home-g295424'), ('Seoul, South Korea','Home-g294197'), \
('Rome, Italy','Home-g187791'), ('Phuket, Thailand','Home-g293920'), ('Guangzhou, China','Home-g298555'), ('Mecca, Saudi Arabia','Home-g293993'), \
('Pattaya, Thailand','Home-g293919'), ('Taipei, Taiwan','Home-g293913'), ('Miami, USA','Home-g34439'), ('Prague, Czech Republic','Home-g274707'), \
('Shanghai, China','Home-g308272'), ('Las Vegas, USA','Home-g45963'), ('Milan, Italy','Home-g187849'), ('Barcelona, Spain','Home-g187497'), \
('Moscow, Russia','Home-g294459'), ('Amsterdam, Netherlands','Home-g188590'), ('Vienna, Austria','Home-g190454'), ('Venice, Italy','Home-g187870'), \
('Los Angeles, USA','Home-g32655'), ('Lima, Peru','Home-g32655'), ('Tokyo, Japan','Home-g298184'), ('Johannesburg, South Africa','Home-g312578'), \
('Beijing, China','Home-g294212'), ('Sofia, Bulgaria','Home-g294452'), ('Orlando, USA','Home-g34515'), ('Berlin, Germany','Home-g187323'), \
('Budapest, Hungary','Home-g274887'), ('Ho Chi Minh City, Vietnam','Home-g293925'), ('Florence, Italy','Home-g187895'), \
('Madrid, Spain','Home-g187514'), ('Warsaw, Poland','Home-g274856'), ('Doha, Qatar','Home-g294008'), ('Nairobi, Kenya','Home-g294207'), \
('Delhi, India','Home-g304551'), ('Mumbai, India','Home-g304554'), ('Chennai, India','Home-g304556'), ('Mexico City, Mexico','Home-g150800'), \
('Dublin, Ireland','Home-g186605'), ('San Francisco, USA','Home-g60713'), ('Hangzhou, China','Home-g298559'), ('Denpasar, Indonesia','Home-g297694'), \
('St. Petersburg, Russia','Home-g298507'), ('Mugla, Turkey','Home-g1221512'), ('Brussels, Belgium','Home-g188644'), ('Burgas, Bulgaria','Home-g635766'), \
('Munich, Germany','Home-g187309'), ('Zhuhai, China','Home-g297418'), ('Sydney, Australia','Home-g255060'), ('Edirne, Turkey','Home-g652369'), ('Toronto, Canada','Home-g155019'), \
('Lisbon, Portugal','Home-g189158'), ('Cancún, Mexico','Home-g150807'), ('Buenos Aires, Argentina','Home-g312741'), ('Cairo, Egypt','Home-g294201'), \
('Punta Cana, Domincan Republic','Home-g147293'), ('Suzhou, China','Home-g297442'), ('Djerba, Tunisia','Home-g297941'), ('Agra, India','Home-g297683'), \
('Kraków, Poland','Home-g274772'), ('Bucharest, Romania','Home-g294458'), ('Siem Reap, Cambodia','Home-g297390'), ('Jaipur, India','Home-g304555'), \
('Honolulu, USA','Home-g60982'), ('Manama, Bahrain','Home-g293997'), ('Dammam, Saudi Arabia','Home-g298547'), ('Hanoi, Vietnam','Home-g293924'), \
('Andorra La Vella, Andorra','Home-g190392'), ('Nice, France','Home-g187234'), ('Zürich, Switzerland','Home-g188113'), \
('Jakarta, Indonesia','Home-g294229'), ('Manila, Philippines','Home-g298573'), ('Chiang Mai, Thailand','Home-g293917'), \
('Marrakech, Morocco','Home-g293734'), ('Sharm El Sheikh, Egypt','Home-g297555'), ('Marne-La-Vallée, France','Home-g226865'), \
('Frankfurt, Germany','Home-g187337'), ('Abu Dhabi, United Arab Emirates','Home-g294013'), ('Vancouver, Canada','Home-g154943'), \
('Guilin, China','Home-g298556'), ('Melbourne, Australia','Home-g255100'), ('Rio De Janeiro, Brazil','Home-g303506'), \
('Riyadh, Saudi Arabia','Home-g293995'), ('Amman, Jordan','Home-g293986'), ('Sousse, Tunisia','Home-g295401'), ('Kiev, Ukraine','Home-g294474'), \
('Sharjah, United Arab Emirates','Home-g298064'), ('Jeju Island, South Korea','Home-g983296'), ('Krabi, Thailand','Home-g297927'), \
('Artvin, Turkey','Home-g652371')]


print(cities)
'''
grade_alphabet = ['A','B','C','D','F']

def time_weight(start, day, end):
    beginning = datetime.strptime(start, "%Y%m%d")
    current = datetime.strptime(day, "%Y%m%d")
    finale = datetime.strptime(end, "%Y%m%d")
    diff = abs((current - beginning).days)
    length = abs((finale - beginning).days)
    time_weight = math.sqrt(diff / length)
    return time_weight

def total_weight(goal, class_results):
    num_results = []
    for result in class_results:
        grade_score = time_weight(day1, result[0], end) * (grade_alphabet.index(result[1]) - grade_alphabet.index(goal))
        num_results.append(grade_score)
    weight = sum(num_results) / len(num_results)
    if weight <= 0:
        weight += -1
    return weight

goal = input('Please enter desired grade: ')
c_r = ['A','B','B','A']
print(weight(goal, c_r))
'''

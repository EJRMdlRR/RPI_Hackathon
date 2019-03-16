from datetime import datetime
import math

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

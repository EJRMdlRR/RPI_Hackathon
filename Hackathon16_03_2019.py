grade_alphabet = ['A','B','C','D','F']

def weight(class_results):
    num_results = []
    for result in class_results:
        grade_score = grade_alphabet.index[result] - grade_alphabet.index[goal]
        num_results.append(grade_score)
    weight = sum(num_results) / len(num_results)

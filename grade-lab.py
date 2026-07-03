def calculate_grade(scores):
    if not scores:
        return "N/A", 0  

    total = sum(scores)
    average = total / len(scores)
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
    return grade, average

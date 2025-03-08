# Process an list of student scores and assign letter grades.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C 
# 60-69	D
# 0-59	F

import statistics

# A list of student scores, where each item represents cumulative
# scores for a single student. This is the kind of data that might be
# obtained from a database query.

student_scores = [
    { "ID": "0001", "scores": [95, 93, 94, 100] },
    { "ID": "0002", "scores": [76, 82, 80, 75] },
    { "ID": "0003", "scores": [80, 82, 79, 81] },
    { "ID": "0004", "scores": [60, 75, 64, 72] },
]


# Average an array of scores and assigns a corresponding letter grade.

def grade_suffix(avg):
    mod = avg % 10

    if mod >=0 and mod <= 3:
        suffix = "-"
    elif mod >=7 and mod <=9:
        suffix = "+"
    else:
        suffix = ""

    return suffix

def letter_grade(avg):      
    if avg >= 90:
        grade = "A" + grade_suffix(avg)
    elif avg >= 80 and avg <= 89:
        grade = "B" + grade_suffix(avg)
    elif avg >= 70 and avg <= 79: 
        grade = "C" + grade_suffix(avg)
    elif avg >= 60 and avg <= 69:
        grade = "D" + grade_suffix(avg)
    else:
        grade = "F"

    return grade
    

for score_list in student_scores:
    avg = int(statistics.mean(score_list["scores"]))
    grade = letter_grade(avg)

    # Save the computed data into the list (assuming it might be written back to a database).
    score_list["average"] = avg
    score_list["letter_grade"] = grade

    # Log output
    print(f"Student {score_list['ID']}: average score {avg}, letter grade {grade}")

# Print the modified list for demonstration purposes
print(student_scores)




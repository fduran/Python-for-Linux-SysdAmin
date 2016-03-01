# Find stats (max, average) from a scores.txt files of the form:
# student_name score
# student_name score
# where student_name can be repeated and score is a numerical value

# Solution:
# 1. read file, get values in dictionary of lists like:
# grades = { "joe": [2, 4.5], 
#           "mary": [0.3, 3.4, 6.7],
#           "tom": [3]
#          }


grades = {}
with open("scores.txt") as fd:
    for line in fd:
        line.strip()
        student, score = line.split()
        score = float(score)
        print student, score
        if not grades.get(student):
            grades[student] = [score]
        else:
            grades[student].extend([score])


print "Grades: ", grades
            
# 2. calculate stats
L = []
max_value = 0.0
for k, vlist in grades.items():
    # find max score, student with max score
    if max(vlist) > max_value:
        max_value = max(vlist)
        max_student = k
    # get all scores in a list
    L.extend(vlist)

# average
ave = sum(L) / len(L)

print "Max score: %.2f" %max_value
print "Max student: %s" %max_student
print "Average score: %.2f" %ave
    

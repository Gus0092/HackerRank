#https://www.hackerrank.com/challenges/grading/problem
#Dificuldade: Facil
def gradingStudents(grades):
    for i in range (len(grades)):
        if grades[i]%5>2 and grades[i]>37:
            grades[i] = grades[i] + (5-((grades[i])%5))
    return (grades)
'''
    HL University has the following grading policy: Every student receives a grade in the inclusive range of 0 - 100
    Any grade less than 40 is a failing grade.
    Sam is a professor at the university and likes to round each student's grade according to these rules:
    If the difference between the grade and the next multiple of 5 is less than 3, round up to the next multiple of 5.
    If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
'''


def grading_students(n):
    for i in range(len(n)):
        if n[i] > 37:
            if ((n[i] % 5) != 0):
                if (5-(n[i] % 5) < 3):
                    n[i] += 5-(n[i] % 5)

    print(n)

example = [54, 33, 78, 97, 42]
grading_students(example)

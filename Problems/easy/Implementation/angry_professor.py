'''
    A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline,
    the professor decides to cancel class if fewer than some number of students are present when class starts.
    Arrival times go from on time (arrivalTime<=0) to arrived late (arrivalTime>0).
    Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled.
'''

def angryProfessor(k, a):
    ontime_count = 0
    for i in range(len(a)):
        if a[i] <= 0:
            ontime_count += 1
        else:
            pass

    if ontime_count >= k:
        print("NO")
    else:
        print("YES")


# test cases
a = [-1, -3, 4, 2]
b = [0, -1, 2, 1]

angryProfessor(3, a)
angryProfessor(2, b)
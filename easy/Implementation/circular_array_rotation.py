"""
    John Watson knows of an operation called a right circular rotation on an array of integers.
    One rotation operation moves the last array element to the first position and shifts all remaining elements right one.
    To test Sherlock's abilities, Watson provides Sherlock with an array of integers.
    Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.
    For each array, perform a number of right circular rotations and return the values of the elements at the given indices.

    int a[n]: the array to rotate
    int k: the rotation count
    int queries[1]: the indices to report
"""


def circularArrayRotation(a, k, queries):


    result = []
    for l in range(k):
        last_number = a[-1]
        a.remove(last_number)
        a.insert(0, last_number)

        l += 1
    for q in queries:
        result.append(a[q])

    print(a)
    print(result)


# this one works
def test(a, k, queries):
    n = len(a)
    result = []
    for q in queries:
        result.append(a[(n - k + q) % n])
    print(result)


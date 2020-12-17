'''
    You have been asked to help study the population of birds migrating across the continent.
    Each type of bird you are interested in will be identified by an integer value.
    Each time a particular kind of bird is spotted, its id number will be added to your array of sightings.
    You would like to be able to find out which type of bird is most common given a list of sightings.
    Your task is to print the type number of that bird and if two or more types of birds are equally common,
    choose the type with the smallest ID number
'''



arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

def migratory(arr):
    bird_frequency = [0,0,0,0,0,0]  #this is because we have 5 maximume of bird types
    for i in range(len(arr)):
        bird_frequency[arr[i]] += 1
    return bird_frequency.index(max(bird_frequency))
'''
    index : The index() method returns the lowest index in list that obj appears.
    it means we want the lowest number of the list that have max frequency of birds
'''

migratory(arr)
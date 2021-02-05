def tripLength(tripList):
    """
    Using a list of cities in the order they were visited,
    the total trip length is calculated.
    """
    #Create the initial list that will be used later on in the program
    cities, distances = getLists()

    #trip will be our running total of the trip length
    trip = 0

    #Will run only when the length of tripList is greater than 2
    while len(tripList) > 2:

        #The currentCity and nextCity are set to the values in tripList
        currentCity = tripList[0]
        nextCity = tripList[1]

        #using currentCity and nextCity, we find the index using the cities list
        currentIndex = cities.index(currentCity)
        nextIndex = cities.index(nextCity)

        #using the calcDistance function, we determine distnace to add onto trip
        trip = trip + findDistance(currentIndex, nextIndex, distances)
        del tripList[0]

    #this portion will run once the list is down to 2 entries
    #it is the same method used within the while loop
    #if it were within the while loop, it would bring the list length down to 1
    currentIndex = cities.index(tripList[0])
    nextIndex = cities.index(tripList[1])

    #trip is increased one more time
    trip = trip + findDistance(currentIndex, nextIndex, distances)

    #trip is returned and will be equal to the trip length
    return trip
                  
def getLists():
    """
    The 2 lists that we need are created from the distances text file
    """
    #two empty lists are made and the file is opened
    cities = []
    distances = []
    file = open("distances.txt","r")

    #Each line will be iterated over
    for line in file:

        #each line will be split into 2 strings at the first space
        city, dist = line.split(" ",1)

        #since city does not need any further work, it will be appended to the cities list
        cities.append(city)

        #dist is a string made of numbers, so the default split is used to turn it into a list
        dist = dist.split()

        #that list is then appended to the distances list
        distances.append(dist)

    #the file is closed and then the lists are returned
    file.close()
    return cities, distances

def findDistance(index1, index2, distList):
    """
    The distance between the 2 cities is found using their index values
    """
    
    #since the max amount of values within the distance list is equal to the index of the city,
    #there will be times when using the standard order will result in the index being out of range

    #so, is index1 is ever greater than index 2, the values are reversed
    #this is because Raleigh to Wilmington is always the same as Wilmington to Raleigh
    if index1 < index2:
        
        #distance is set to the value within the distList
        distance = int(distList[index2][index1])
    else:
        distance = int(distList[index1][index2])

    #the value is then returned 
    return distance
        

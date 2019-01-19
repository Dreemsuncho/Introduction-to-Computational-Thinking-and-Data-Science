###########################
# 6.0002 Problem Set 1a: Space Cows
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

# ================================
# Part A: Transporting Space Cows
# ================================


# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    import re

    file = open(filename)

    arr = re.split('[,\n]', file.read())

    file.close()

    cows = {}
    for i in range(0, len(arr), 2):
        cow_name = arr[i]
        cow_weight = arr[i + 1]
        cows[cow_name] = int(cow_weight)

    return cows


# Problem 2
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    import operator

    totalTrips = []
    sorted_cows = sorted(
        [(name, weight)
         for name, weight in cows.items()
         if cows[name] <= limit],
        key=operator.itemgetter(1),
        reverse=True
    )

    repeat = True
    while repeat:
        currentTrip = []
        currentTotal = 0

        for name, weight in sorted_cows:
            if currentTotal+weight <= limit:
                currentTrip.append(name)
                currentTotal += weight

        for name in currentTrip:
            cow = (name, cows[name])
            sorted_cows.remove(cow)

        totalTrips.append(currentTrip)
        repeat = len(sorted_cows) > 0

    return totalTrips


# Problem 3
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    for partition in sorted(get_partitions(cows), key=len):

        exceed = False
        for trip in partition:

            trip_weight = 0
            for cow in trip:
                if trip_weight+cows[cow] > limit:
                    exceed = True
                    break
                trip_weight += cows[cow]

            if exceed:
                break

        if not exceed:
            return partition

    return best_trips


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows(filename='ps1_cow_data.txt')

    start = time.time()
    greedy_result = greedy_cow_transport(cows)
    end = time.time()

    greedy_time = end - start

    #
    start = time.time()
    brute_force_result = brute_force_cow_transport(cows)
    end = time.time()

    brute_force_time = end - start

    print("Input:", cows)

    print("Greedy:")
    print(" - result", greedy_result)
    print(" - time", greedy_time)

    print("Brute force:")
    print(" - result", brute_force_result)
    print(" - time", brute_force_time)


compare_cow_transport_algorithms()


# Problem 5
# Answer the following questions.

# 1. What were your results from compare_cow_transport_algorithms? Which algorithm runs faster? Why?
# Answer:
    # Comparing the greedy and brute force algorithms, we see a lot of difference, brute force run much slower, because have to enumerate all possibilities before choose the best one.

# 2. Does the greedy algorithm return the optimal solution? Why/why not?
# Answer:
    # Not it doesn't, because greedy is really greedy, it uses the first optimal solution that finds and does not try other possibilities.

# 3. Does the brute force algorithm return the optimal solution? Why/why not?
# Answer:
    # Yes of course, brute force algorithm always will return one of the optimal solutions, if has more than one and the reason is, because the algorithm will generate every possible outcome before decide which one is optimal.

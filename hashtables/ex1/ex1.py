cache = {}


def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    this is possibly similiar to the lookup hash table with an extra step of seeing if the limit is matched with the values

    find 2 items whose added weight == limit
     want the index of the numbers
     weights is a list
     length is the length of the list(weights)
     limit is what I want the two numbers to equal
      Should iterate over weights and add the numbers to figure out which pair equals the limit
        if == limit spit out the highest(max) number index first then the Lowest (min) number last

    highest value should be first, smallest value should be next

    make a cache to store variables
    """
# Your code here
# iterating over the length of list weights and staying in that range
    for i in range(len(weights)):
        # i for index
        cache[weights[i]] = i  # put in the cache
    for i in range(len(weights)):  # iterate over weight again
        x = limit - weights[i]  # x = limit - weight index
        if x in cache:  # for numbers in cache
            # give (highest #, lowest #) of the numbers index
            print(' i want to see: ', max(i, cache[x]), min(i, cache[x]))
            return (max(i, cache[x]), min(i, cache[x]))

    return None

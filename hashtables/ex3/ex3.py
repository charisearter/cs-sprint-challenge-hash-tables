def intersection(arrays):
    """
    YOUR CODE HERE

    Find the common number in all the lists ???
    Possibly have a dictionary cache to  hold each number and then when it gets to end, see which number count matches the amount of lists -> menaing that number was in all the lists

    cannot use numpy or set

    similar to word count project
    """
    # Your code here
    cache = {}  # empty dictionary to hold counter of numbers
    result = []  # place for the results
    l = len(arrays)  # i need to know the length of the array of lists
    count = 1  # counter to see how many times a number pops up...initial count not in cache is 1

    for allLists in arrays:  # iterate over every list in array
        for x in allLists:  # look at each item in the lists
            if x not in cache:  # if that item is not in the cache
                # add it to the cache with the initial count x:1
                cache[x] = count
            else:  # otherwise if allready in the cache
                cache[x] += 1  # add 1 to the count
    for nums in cache:  # iterate over all the numbers in the cache
        if cache[nums] == l:  # if thenum value is equal to the length
            result.append(nums)  # add the number to the result list
    print('ex3 results: ', result)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

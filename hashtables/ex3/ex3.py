def intersection(arrays):
    """
    YOUR CODE HERE
    
    Find the common number in all the lists ???
    Possibly have a dictionary cache to input hold each number and then when it gets to end, see which number count matches the amount of lists -> menaing that number was in all the lists
    """
    # Your code here

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


cache = {}  # empty dictionary to recheck values already added


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    Link the tickets
     1st ticket => source == None  destination of 1st ticket == 2nd tickets source
     The next tickets source == previous tickets destination
     Final ticket destination == None
     If the destination of last ticket and source to next ticket match, the next ticket should be listed after the destination ticket
     should iterate over list checking current destination to next.source
     if source == None ... prepend to list (make sure it is first)
     if destination == None ... append to end of list, len(self -1) make sure it is last
     if current.destination == next.source
     next.source. append to list
    """
    # Your code here

    route = [None] * length  # make an empty route list to match the length

    for t in tickets:  # for each ticket in the tickets
        # add source:destination of each to cache
        cache[t.source] = t.destination
    # make next location destination to starting location for next ticket
    next = cache["NONE"]  # make sure all caps otherwise does not work
    for i in range(0, length):  # start at index 0 and go thru length
        route[i] = next
    # make next value be current place, next place to go in cache
        next = cache[next]
    print('I wanna see: ', route)
    return route

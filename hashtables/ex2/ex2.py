#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    Link the tickets
     1st ticket => source == None  destination of 1st ticket == 2nd tickets source
     The next tickets source == previous tickets destination
     Final ticket destination == None
    
    """
    # Your code here

    return route

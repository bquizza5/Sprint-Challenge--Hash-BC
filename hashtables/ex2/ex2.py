#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length) #source --> destination
    hashtable2 = HashTable(length) #destination --> source
    route = [None] * length
    
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)


    for ticket in tickets:
        hash_table_insert(hashtable2, ticket.destination, ticket.source)

    start = hash_table_retrieve(hashtable, "NONE")
    next1 = start
    print(next1)
    index = 0
    while next1 != "NONE":
        route[index] = next1
        next1 = hash_table_retrieve(hashtable, next1)
        index += 1
    route[-1] = "NONE"
    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

expected = ["PDX", "DCA", "NONE"]
result = reconstruct_trip(tickets, 3)

print(result)
#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    index= 0
    for weight in weights:
        hash_table_insert(ht,weight, index)
        index += 1

    for weight in weights:
        weight2 = limit - weight
        if hash_table_retrieve(ht, weight2):
            if hash_table_retrieve(ht, weight) >= hash_table_retrieve(ht, weight2):
                return (hash_table_retrieve(ht, weight), hash_table_retrieve(ht, weight2))
            else:
                return (hash_table_retrieve(ht, weight2), hash_table_retrieve(ht, weight))
        else:
            None
    
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")



weights_2 = [4, 4]
print(get_indices_of_item_weights(weights_2, 2, 8))


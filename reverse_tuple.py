def reverse_tuple(tuple_set1, tuple_set2):
    for set in tuple_set1:
        newset = (set[1],set[0])
        if newset in tuple_set2:
            return True
    return False

print(reverse_tuple({(1, 2), (3, 4)}, {(2, 1), (5, 6)}))
print("----")
print(reverse_tuple({(1, 2), (3, 4)}, {(1, 2), (2, 3)}))
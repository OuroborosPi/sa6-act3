list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
list_two = [2, 4, 6, 8, 10, 12, 14]

# Use filter to keep elements from list_one that are also in list_two
result = list(filter(lambda x: x in list_two, list_one))
print(f'Intersection of the two list is: {result}')

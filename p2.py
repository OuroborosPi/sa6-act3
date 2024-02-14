string_list = ['Hello','Cat','Dog','Elephant','pneumonoultramicroscopicsilicovolcanoconiosis','Bird','Tiger']
list_sorter = sorted(string_list, key= lambda x: len(x))
print(f'The list sorted by length: {list_sorter}')

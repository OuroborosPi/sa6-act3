list_numbers = [4, 54, 78, 223, 76, 23, 0, -1, -400, 67, 0]
comparison_function = lambda x, y: x if x > y else y  # lambda with simple if comparison 

def find_maximum(list_numbers, comparison_function):
    max_number = list_numbers[0]  # initialize the maximum with the first element of the list
    for number in list_numbers[1:]:  # start the loop from the second element
        max_number = comparison_function(max_number, number)  # use the lambda function to update the maximum
    return max_number

print(f'Max number is: {find_maximum(list_numbers, comparison_function)}')

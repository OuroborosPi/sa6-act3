numbers = [4,7,9,12,20,40]
n = 5

result = list(map(lambda x: x**n,numbers)) #takes the anon function that uses n as the power for the list numbers
print(result)

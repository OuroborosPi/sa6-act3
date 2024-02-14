num = 456
sum_digits = lambda num: sum(int(n) for n in str(num) if n.isdigit())
print (f'The sum of the number is:{sum_digits(num)}')

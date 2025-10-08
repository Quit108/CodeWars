operator=input('Enter operator: ')
value1=int(input('Enter first value: ')) 
value2=int(input('Enter second value: '))

def basic_op(operator, value1, value2):
    return {'+': value1 + value2, '-': value1 - value2, '*': value1 * value2, '/': value1 / value2}[operator]

print(basic_op(operator, value1, value2)) 
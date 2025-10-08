a=int(input('Enter first number: '))
b=int(input('Enter second number: '))

def add_binary(a,b):
    return bin(a+b).replace('0b','')

print(add_binary(a,b), type(add_binary(a,b)))
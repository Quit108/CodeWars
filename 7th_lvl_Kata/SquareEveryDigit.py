num=int(input('Enter a number: '))

def square_digits(num):
    return int(''.join(str(int(digit) ** 2) for digit in str(num)))

print(square_digits(num))
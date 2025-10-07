base=int(input('Enter the base number: '))
factor=int(input('Enter the factor number: '))

def check_for_factor(base, factor):
    return base % factor == 0

print(check_for_factor(base, factor))